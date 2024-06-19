import os, struct, sys
from math import log
from uuid import UUID

from ctypes import POINTER, byref, cast, c_int, c_void_p, create_string_buffer, windll, oledll, pointer, c_ubyte, c_char_p
from ctypes.wintypes import LONG, RECT, DWORD

from dshow.comtypes import GUID, STDMETHOD, HRESULT, IUnknown, CoCreateInstance, CreateObject, IClassFactory
from dshow.comtypes.hresult import *
from dshow.lib import *


WS_CHILD = 1073741824
WS_CLIPSIBLINGS = 67108864
WS_CLIPCHILDREN = 33554432

winmm = windll.Winmm

########################################
#
########################################
def _raw_guid(guid):
    """Given a string GUID or a pythoncom IID, return the GUID laid out in memory suitable for passing to ctypes"""
    return UUID(str(guid)).bytes_le

########################################
#
########################################
def _create_object_from_path(clsid, dll_filename, interface=IBaseFilter):
    clsid_class = _raw_guid(clsid)
    iclassfactory = _raw_guid(IClassFactory._iid_)
    my_dll = oledll.LoadLibrary(dll_filename)
    factory_ptr = c_void_p(0)
#    HRESULT DllGetClassObject(
#      [in]  REFCLSID rclsid,
#      [in]  REFIID   riid,
#      [out] LPVOID   *ppv
#    );
    my_dll.DllGetClassObject.argtypes = (c_char_p, c_char_p, LPVOID)
    my_dll.DllGetClassObject(clsid_class, iclassfactory, byref(factory_ptr))
    ptr_icf = POINTER(IClassFactory)(factory_ptr.value)
    pUnk = ptr_icf.CreateInstance()
    return pUnk.QueryInterface(interface)


########################################
#
########################################
class Player():

    ########################################
    #
    ########################################
    def __init__(self, hwnd=None, width=0, height=0, volume=.75, keepaspectratio=True,
            use_local_filters=True, use_lav_decoders=True, use_vmr_windowless=False,
            use_master_volume=True, filter_dir=None):

        self._parent_hwnd = hwnd
        self._width = width
        self._height = height
        self._keepaspectratio = keepaspectratio
        self._use_local_filters = use_local_filters
        self._use_lav_decoders = use_lav_decoders
        self._use_vmr_windowless = use_vmr_windowless
        self._use_master_volume = use_master_volume

        if self._use_master_volume:
            # don't change master volume here
            self.get_volume()
        else:
            self._volume = volume

        self._balance = 0
        self._frame_step = 0
        self._filter_dir = (filter_dir if filter_dir else
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'filters'))

        self._vmr_mixer_control9 = None
        self._vmr_windowless_control9 = None
        self._vmr_aspect_control = None
        self._basic_audio = None
        self._basic_video = None
        self._media_control = None
        self._media_event = None
        self._media_seeking = None
        self._video_window = None
        self._filter_graph = None

        self._has_video = False
        self._has_audio = False

    ########################################
    #
    ########################################
    def has_video(self):
        return self._has_video

    ########################################
    #
    ########################################
    def has_audio(self):
        return self._has_audio

    ########################################
    #
    ########################################
    def set_use_master_volume(self, flag):
        self._use_master_volume = flag

    ########################################
    #
    ########################################
    def _create_filtergraph(self):
        self._filter_graph = CreateObject(CLSID_FilterGraph, interface=IFilterGraph)

    ########################################
    # TEST
    ########################################
    def _query_interfaces(self):
        self._media_control = self._filter_graph.QueryInterface(IMediaControl)
        self._media_event = self._filter_graph.QueryInterface(IMediaEventEx)
        self._media_seeking = self._filter_graph.QueryInterface(IMediaSeeking)
        if self._has_video:
            self._basic_video = self._filter_graph.QueryInterface(IBasicVideo)
            if not self._use_vmr_windowless:
                self._video_window = self._filter_graph.QueryInterface(IVideoWindow)
        if self._has_audio:
            self._basic_audio = self._filter_graph.QueryInterface(IBasicAudio)

    ########################################
    # was: _delete_interfaces
    ########################################
    def _reset(self):
        if self._vmr_mixer_control9:
            del self._vmr_mixer_control9
            self._vmr_mixer_control9 = None

        if self._vmr_aspect_control:
            del self._vmr_aspect_control
            self._vmr_aspect_control = None

        if self._basic_audio:
            del self._basic_audio
            self._basic_audio = None

        if self._basic_video:
            del self._basic_video
            self._basic_video = None

        if self._media_control:
            del self._media_control
            self._media_control = None

        if self._media_event:
            del self._media_event
            self._media_event = None

        if self._media_seeking:
            del self._media_seeking
            self._media_seeking = None

        if self._video_window:
            self._video_window.Visible = False
            # Reset the owner to NULL before releasing the Filter Graph Manager
            self._video_window.Owner = 0
            self._video_window.MessageDrain = 0

            del self._video_window
            self._video_window = None

        if self._filter_graph:
            enum = self._filter_graph.EnumFilters()
            while True:
                filt, fetched = enum.Next(1)
                if not fetched:
                    break
                self._filter_graph.RemoveFilter(filt)
                ###filt.Release()
                enum.Reset()

            del self._filter_graph
            self._filter_graph = None

        self._has_video = False
        self._has_audio = False

    ########################################
    #
    ########################################
    def _get_pin_by_name (self, filt, pinName):
        enum = filt.EnumPins()
        while True:
            pin, fetched = enum.Next(1)
            if not fetched:
                break
            pinInfo = pin.QueryPinInfo()
            if pinName in ''.join(map(chr, pinInfo.achName)):
                return pin

    ########################################
    #
    ########################################
    def _get_unconnected_pin (self, filt, direction):
        enum = filt.EnumPins()
        while True:
            pin, fetched = enum.Next(1)
            if not fetched:
                break
            d = pin.QueryDirection()
            if d == direction:
                try:
                    tmp = pin.ConnectedTo()
                    # Already connected - not the pin we want
                    continue
                except:
                    return pin

    ########################################
    #
    ########################################
    def _build_graph (self, src_file, use_local_filters=True, use_lav_decoders=True, add_directvobsub=False):

        # Add LAV Splitter Source
        lav_splitter_source = (_create_object_from_path(CLSID_LAVSplitterSource,
                os.path.join(self._filter_dir, 'LAVSplitter.ax'))
                if use_local_filters else CreateObject(CLSID_LAVSplitterSource, interface = IBaseFilter))

        self._filter_graph.AddFilter(lav_splitter_source, 'LAV Splitter Source')

        # Set source filename
        lav_splitter_source_src = lav_splitter_source.QueryInterface(IFileSourceFilter)
        try:
            lav_splitter_source_src.Load(src_file, None)
        except:
            print('dshow._build_graph failed')
            return False

        # default to 100ms
        self._frame_step = 1000000

        try:
            pin_out_src_video = self._get_pin_by_name(lav_splitter_source, 'Video')
        except:
            #print('no video found')
            pin_out_src_video = None

        try:
            pin_out_src_audio = self._get_pin_by_name(lav_splitter_source, 'Audio')
        except:
            #rint('no audio found')
            pin_out_src_audio = None

        if pin_out_src_video is not None:
            # Add Video Decoder
            if use_lav_decoders:
                video_decoder = (_create_object_from_path(CLSID_LAVVideoDecoder,
                        os.path.join(self._filter_dir, 'LAVVideo.ax'))
                        if use_local_filters else CreateObject(CLSID_LAVVideoDecoder, interface = IBaseFilter))
                self._filter_graph.AddFilter(video_decoder, 'LAV Video Decoder')
            else:
                video_decoder = CreateObject(CLSID_MsDTVDVDVideoDecoder, interface = IBaseFilter)
                self._filter_graph.AddFilter(video_decoder, 'MsDTVDVDVideoDecoder')

            # Add VMR-9 Video Renderer
            video_mixing_renderer = CreateObject(CLSID_VideoMixingRenderer9, interface = IBaseFilter)

            if self._use_vmr_windowless:
                cfg = video_mixing_renderer.QueryInterface(IVMRFilterConfig9)
                cfg.SetNumberOfStreams(2)
                cfg.SetRenderingMode(VMR9Mode_Windowless)
                self._vmr_windowless_control9 = video_mixing_renderer.QueryInterface(IVMRWindowlessControl9)
                self._vmr_windowless_control9.SetVideoClippingWindow(self._parent_hwnd)

            else:
                self._vmr_aspect_control = video_mixing_renderer.QueryInterface(IVMRAspectRatioControl9)

            self._filter_graph.AddFilter(video_mixing_renderer,
                    'Video Mixing Renderer 9' + (' (windowless)' if self._use_vmr_windowless else ''))

            # Connect LAV Splitter Source and LAV Video Decoder
            pin_in_video_decoder = self._get_pin_by_name(video_decoder, 'In')
            self._filter_graph.ConnectDirect(pin_out_src_video, pin_in_video_decoder, None)

            # Connect LAV Video Decoder and Video Mixing Renderer
            pin_out_video_decoder = self._get_pin_by_name(video_decoder, 'Out')
            pin_in_video_renderer = self._get_pin_by_name(video_mixing_renderer, 'VMR Input0')
            self._filter_graph.ConnectDirect(pin_out_video_decoder, pin_in_video_renderer, None)

            # get framerate
            pmt = pin_out_src_video.ConnectionMediaType()
            formattype = str(pmt.formattype)
            if formattype == FORMAT_VideoInfo2 or formattype == FORMAT_MPEG2_VIDEO:
                vh = cast(pmt.pbFormat, POINTER(VIDEOINFOHEADER2))
                self._frame_step = vh.contents.AvgTimePerFrame

            elif formattype == FORMAT_VideoInfo or formattype == FORMAT_MPEGVideo:
                vh = cast(pmt.pbFormat, POINTER(VIDEOINFOHEADER))
                self._frame_step = vh.contents.AvgTimePerFrame

            self._vmr_mixer_control9 = video_mixing_renderer.QueryInterface(IVMRMixerControl9)

            pin_out_src_video.Release() # for some reason only the splitter pins have to be released explicitely!

            self._has_video = True

        if pin_out_src_audio is not None:
            # Add Audio Decoder
            if use_lav_decoders:
                audio_decoder = (_create_object_from_path(CLSID_LAVAudioDecoder,
                        os.path.join(self._filter_dir, 'LAVAudio.ax'))
                        if use_local_filters else CreateObject(CLSID_LAVAudioDecoder, interface = IBaseFilter))
                self._filter_graph.AddFilter(audio_decoder, 'LAV Audio Decoder')
            else:
                audio_decoder = CreateObject(CLSID_MsDTVDVDAudioDecoder, interface = IBaseFilter)
                self._filter_graph.AddFilter(audio_decoder, 'MsDTVDVDAudioDecoder')

            # Add DirectSound Audio Renderer
            directsound_audio_renderer = CreateObject(CLSID_DirectSoundAudioRenderer, interface = IBaseFilter)
            self._filter_graph.AddFilter(directsound_audio_renderer, 'DirectSound Audio Renderer')

            # Connect LAV Splitter Source and Audio Decoder
            pin_in_audio_decoder = self._get_pin_by_name(audio_decoder, 'Input' if use_lav_decoders else 'XForm In')
            self._filter_graph.ConnectDirect(pin_out_src_audio, pin_in_audio_decoder, None)

            # Connect Audio Decoder and DirectSound Audio Renderer
            pin_out_audio_decoder = self._get_pin_by_name(audio_decoder, 'Output' if use_lav_decoders else 'XFrom Out')
            pin_in_audio_renderer = self._get_pin_by_name(directsound_audio_renderer, 'Audio Input pin (rendered)')
            self._filter_graph.ConnectDirect(pin_out_audio_decoder, pin_in_audio_renderer, None)

            pin_out_src_audio.Release() # for some reason only the splitter pins have to be released explicitely!

            self._has_audio = True

        return True

    ########################################
    # No direct return value!
    ########################################
    def load_file(self, fn, use_local_filters=True, use_lav_decoders=True, use_vmr_windowless=None):

        if use_vmr_windowless is not None:
            self._use_vmr_windowless = use_vmr_windowless
        if use_local_filters is not None:
            self._use_local_filters = use_local_filters
        if use_lav_decoders is not None:
            self._use_lav_decoders = use_lav_decoders

        self.close_file()

        self._create_filtergraph()

        if not self._build_graph(fn, self._use_local_filters, self._use_lav_decoders):
            self._filter_graph = None
            return False

        self._query_interfaces()

        # setup videowindow
        if self._has_video:

            if self._use_vmr_windowless:
                dest_rect = RECT(0, 0, self._width, self._height)
                self._vmr_windowless_control9.SetVideoPosition(None, byref(dest_rect))
            else:
                self._video_window.Owner = self._parent_hwnd
                self._video_window.WindowStyle = WS_CHILD | WS_CLIPCHILDREN | WS_CLIPSIBLINGS
                self._video_window.SetWindowPosition(0, 0, self._width, self._height)
                self._video_window.MessageDrain = self._parent_hwnd

            self.set_keepaspectratio(self._keepaspectratio)

        if self._has_audio:
            self.set_volume(self._volume)

        #self._media_control.Run()

        return True

    ########################################
    # Render file with GraphBuilder
    ########################################
    def render_file(self, fn):

        self.close_file()

        self._create_filtergraph()

        graph_builder = self._filter_graph.QueryInterface(IGraphBuilder)

        try:
            graph_builder.RenderFile(fn, None)
        except:
            print('graph_builder.RenderFile in dshow.render_file failed')
            self._filter_graph = None
            return False

        self._query_interfaces()

        # default to 100ms
        self._frame_step = 1000000

        if self._basic_video:
            try:
                self._video_window.Owner = self._parent_hwnd
                self._video_window.WindowStyle = WS_CHILD | WS_CLIPCHILDREN | WS_CLIPSIBLINGS
                self._video_window.SetWindowPosition(0, 0, self._width, self._height)
                self._video_window.MessageDrain = self._parent_hwnd

                # find framerate
                if self._media_seeking is not None:
                    tf = str(self._media_seeking.getTimeFormat())
                    if tf == TIME_FORMAT_FRAME:
                        self._frame_step = 1
                    elif self._basic_video is not None and tf == TIME_FORMAT_MEDIA_TIME:
                        try:
                            self._frame_step = int(self._basic_video.AvgTimePerFrame * 10000000)
                        except:
                            #print('self._basic_video.AvgTimePerFrame in dshow.render_file failed')
                            pass

                # find VMR-7 (RenderFile never uses VMR-9 or EVR)
                enum = self._filter_graph.EnumFilters()
                while True:
                    filt, fetched = enum.Next(1)
                    if not fetched:
                        break
                    clsid = str(filt.GetClassID())
                    if clsid == CLSID_VideoMixingRenderer:
                        self._vmr_aspect_control = filt.QueryInterface(IVMRAspectRatioControl)
                        break

                if self._vmr_aspect_control:
                    self.set_keepaspectratio(self._keepaspectratio)

                self._has_video = True

            except:
                print('dshow.render_file failed')
                return False

        if self._basic_audio:
            try:
                self.set_volume(self._volume)
                self._has_audio = True
            except:
                print('dshow.render_file failed')
                return False

        self._media_control.Run()

        return True

    ########################################
    #
    ########################################
    def close_file(self):
        if self._media_control is not None:
            self._media_control.Stop()
        self._reset()

    ########################################
    #
    ########################################
    def resize(self, w, h):
        self._width, self._height = w, h
        if self._has_video:
            if self._use_vmr_windowless:
                dest_rect = RECT(0, 0, w, h)
                return SUCCEEDED(self._vmr_windowless_control9.SetVideoPosition(None, byref(dest_rect)))
            else:
                return SUCCEEDED(self._video_window.SetWindowPosition(0, 0, w, h))

    ########################################
    # State_Stopped = 0,
    # State_Paused = 1
    # State_Running = 2
    ########################################
    def get_state(self):
        if self._media_control:
            return self._media_control.getState(10000)

    ########################################
    #
    ########################################
    def pause(self):
        if self._media_control is None:
            raise Exception('E_NOINTERFACE')
        self._media_control.Pause()

    ########################################
    #
    ########################################
    def play(self):
        if self._media_control is None:
            raise Exception('E_NOINTERFACE')
        self._media_control.Run()

    ########################################
    #
    ########################################
    def toggle_playback (self):
        if self.get_state() == State_Running:
            return self.pause()
        else:
            return self.play()

    ########################################
    #
    ########################################
    def stop(self):
        if self._media_control is None:
            return False
        #self._media_control.Stop()
        self._media_control.Pause()
        self.set_time(0)
        return True

    ########################################
    #
    ########################################
    def step(self, frames=1):
        if self._media_seeking is None or self._frame_step == 0:
            return False
        pos = max(0, self._media_seeking.GetCurrentPosition() + frames * self._frame_step)
        self._media_seeking.SetPositions(pos, AM_SEEKING_AbsolutePositioning, 0, AM_SEEKING_NoPositioning)
        return True

    ########################################
    # returns ms as float
    ########################################
    def get_duration(self):
        if self._media_seeking is None:
            raise Exception('E_NOINTERFACE')
        return self._media_seeking.getDuration() / 10000.0

    ########################################
    #
    ########################################
    def get_size(self):
        if not self._has_video: #self._basic_video is None:
            raise Exception('E_NOINTERFACE')
        if self._use_vmr_windowless:
            return self._vmr_windowless_control9.GetNativeVideoSize()[:2]
        else:
            return self._basic_video.GetVideoSize()

    ########################################
    # not implemented yet for self._use_vmr_windowless
    ########################################
    def get_fps(self):
        if self._has_video:
            return 10000000 / self._frame_step if self._frame_step > 0 else 0
        else:
            return 0

    ########################################
    # returns ms as float
    ########################################
    def get_time(self):
        if self._media_seeking is None:
            raise Exception('E_NOINTERFACE')
        return self._media_seeking.GetCurrentPosition() / 10000.0

    ########################################
    #
    ########################################
    def set_time(self, ms):
        if self._media_seeking is None:
            raise Exception('E_NOINTERFACE')
        hr, stop_time = self._media_seeking.SetPositions(int(ms*10000),
                AM_SEEKING_AbsolutePositioning, 0, AM_SEEKING_NoPositioning)
        return SUCCEEDED(hr)

    ########################################
    #
    ########################################
    def reload_frame(self):
        if self._media_seeking is None:
            raise Exception('E_NOINTERFACE')
        self._media_seeking.SetPositions(self._media_seeking.GetCurrentPosition(),
                AM_SEEKING_AbsolutePositioning, 0, AM_SEEKING_NoPositioning)

    ########################################
    # fail silently?
    ########################################
    def toggle_fullscreen(self, flag=None):
        if self._video_window is None:
            raise Exception('E_NOINTERFACE')
        if self._use_vmr_windowless:
            return
        if flag is not None:
            self._video_window.FullScreenMode = -1 if flag else 0
        else:
            if self._video_window.FullScreenMode == -1:
                self._video_window.FullScreenMode = 0  # OAFALSE
            else:
                self._video_window.FullScreenMode = -1  # OATRUE

    ########################################
    #
    ########################################
    def is_fullscreen(self):
       if self._video_window is None:
            raise Exception('E_NOINTERFACE')
       return self._video_window.FullScreenMode == -1

    ########################################
    #
    ########################################
    def get_volume(self):
        if self._use_master_volume:
            d = DWORD()
            winmm.waveOutGetVolume(0, byref(d))
            self._volume = (d.value & 0xFFFF) / 0xFFFF
        return self._volume

    ########################################
    # 0..1 => 0..0xffffffff or -10000..0
    ########################################
    def set_volume(self, v, update_state_=True):
        v = max(0, min(1, v))
        if update_state_:
            self._volume = v
        if self._use_master_volume:
            v = int(0xFFFF * v)
            winmm.waveOutSetVolume(0, v | v << 16)
        else:
            if self._has_audio:
                if self._volume == 0:
                    self._basic_audio.Volume = -10000
                else:
                    self._basic_audio.Volume = int(1442.6950 * log(v))

    ########################################
    # The value can range from -10,000 to 10,000
    # -1..1 => -10000..10000
    ########################################
    def set_balance(self, b):
        self._balance = max(-1, min(1, b))
        if self._has_audio:
            self._basic_audio.Balance = self._balance * 10000

    ########################################
    #
    ########################################
    def get_balance(self):
        return self._balance
#        if self._has_audio:
#            return self._basic_audio.Balance

    ########################################
    #
    ########################################
    def get_event(self):
        try:
            # returns (EventCode, Param1, Param2)
            return self._media_event.getEvent(0)[0]
        except:
            return None

    ########################################
    #
    ########################################
    def set_keepaspectratio (self, flag=True):
        self._keepaspectratio = flag
        if self._vmr_windowless_control9:
            return SUCCEEDED(self._vmr_windowless_control9.SetAspectRatioMode(VMR_ARMODE_LETTER_BOX
                    if flag else VMR_ARMODE_NONE))
        elif self._vmr_aspect_control:
            return SUCCEEDED(self._vmr_aspect_control.SetAspectRatioMode(VMR_ARMODE_LETTER_BOX
                    if flag else VMR_ARMODE_NONE))

    ########################################
    #
    ########################################
    def is_seekable(self):
        return self._frame_step > 0

    ########################################
    #
    ########################################
    def get_current_filters (self):
        if self._filter_graph is None:
            raise Exception('E_NOINTERFACE')
        filters = []
        enum = self._filter_graph.EnumFilters()
        while True:
            filt, fetched = enum.Next(1)
            if not fetched:
                break
            clsid = str(filt.GetClassID())
            filter_info = filt.QueryFilterInfo()
            filter_name = ''.join(map(chr, filter_info.achName)).rstrip('\0')
            filters.append([clsid, filter_name])
        return filters
