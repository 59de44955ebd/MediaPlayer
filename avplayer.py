from ctypes import c_void_p

import AVFoundation
from Cocoa import NSURL, NSMakeRect
import CoreMedia
import MediaToolbox
import objc

from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QWidget


class VideoWidget(QWidget):

    mediaReady = pyqtSignal(bool)
    mousePressed = pyqtSignal()
    doubleClicked = pyqtSignal()

    ########################################
    #
    ########################################
    def __init__(self, parent=None):
        super().__init__()

        self.filename = None

        self._player = None
        self._playerLayer = None

        self._timer = QTimer(self)
        self._timer.setInterval(50)
        self._timer.timeout.connect(self.__check_ready)

        # make window background black
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        # cast QWidget to NSView
        self._view = objc.objc_object(c_void_p=c_void_p(int(self.winId())))
        self._view.setWantsLayer_(True)

        MediaToolbox.MTRegisterProfessionalVideoWorkflowFormatReaders()

    ########################################
    #
    ########################################
    def __check_ready(self):
        status = self._player.currentItem().status()
        if status:
            self._timer.stop()
            if status != 1:
                self.filename = None
            self.mediaReady.emit(status == 1)  # 2 means failed

    ########################################
    #
    ########################################
    def load_media(self, filename: str):
        if self._player is not None:
            self.close_media()
        self.filename = filename
        url = NSURL.fileURLWithPath_(filename)
        self._player = AVFoundation.AVPlayer.playerWithURL_(url)

        # create AVPlayerLayer
        self._playerLayer = AVFoundation.AVPlayerLayer.playerLayerWithPlayer_(self._player)
        g = self.geometry()
        self._playerLayer.setFrame_(NSMakeRect(0, 0, g.width(), g.height()))
        self._playerLayer.setAutoresizingMask_(18)  # kCALayerWidthSizable=2 | kCALayerHeightSizable=16
        self._view.layer().addSublayer_(self._playerLayer)

        self._timer.start()

    ########################################
    #
    ########################################
    def close_media(self):
        self.filename = None
        if self._player:
            self._player.setRate_(0.)
            self._player = None
        if self._playerLayer:
            self._playerLayer.removeFromSuperlayer()
            self._playerLayer = None
        self.repaint()

    ########################################
    #
    ########################################
    def step(self, steps: int=1):
        if self._player is None:
            return
        self._player.currentItem().stepByCount_(steps)

    ########################################
    #
    ########################################
    def get_natural_size(self):
        if self._player is None:
            return
        video_tracks = self._player.currentItem().asset().tracksWithMediaType_(AVFoundation.AVMediaTypeVideo)
        if len(video_tracks):
            size = video_tracks[0].naturalSize()
            return size.width, size.height

    ########################################
    # as seconds
    ########################################
    def get_duration(self):
        if self._player is None:
            return
        cm = self._player.currentItem().duration()
        return cm.value / cm.timescale if cm.timescale else 0

    ########################################
    #
    ########################################
    def get_fps(self):
        if self._player is None:
            return
        video_tracks = self._player.currentItem().asset().tracksWithMediaType_(AVFoundation.AVMediaTypeVideo)
        if len(video_tracks):
            return video_tracks[0].nominalFrameRate()

    ########################################
    #
    ########################################
    def has_video(self):
        if self._player is None:
            return
        return len(self._player.currentItem().asset().tracksWithMediaType_(AVFoundation.AVMediaTypeVideo)) > 0

    ########################################
    #
    ########################################
    def has_audio(self):
        if self._player is None:
            return
        return len(self._player.currentItem().asset().tracksWithMediaType_(AVFoundation.AVMediaTypeAudio)) > 0

    ########################################
    # 0..1
    ########################################
    def get_volume(self):
        if self._player is None:
            return 1.0
        return self._player.volume()

    ########################################
    # 0..1
    ########################################
    def set_volume(self, volume: float):
        if self._player is None:
            return
        self._player.setVolume_(float(volume))

    ########################################
    #
    ########################################
    def seek_to_time(self, sec: float):
        if self._player is None:
            return
        cm = self._player.currentItem().duration()
        cm.value = cm.timescale * sec
        self._player.seekToTime_(cm)

    ########################################
    # as seconds
    ########################################
    def get_time(self):
        if self._player is None:
            return
        cm = self._player.currentTime()
        return cm.value / cm.timescale if cm.timescale else 0

    ########################################
    # NEW
    ########################################
    def play(self):
        if self._player is None:
            return
        self._player.setRate_(1.0)

    ########################################
    # NEW
    ########################################
    def pause(self):
        if self._player is None:
            return
        self._player.setRate_(0.0)

    ########################################
    # NEW
    ########################################
    def toggle_playback(self):
        if self._player is None:
            return
        self._player.setRate_(1 - self._player.rate())

    ########################################
    #
    ########################################
    def mousePressEvent(self, e):
        self.mousePressed.emit()

    ########################################
    #
    ########################################
    def mouseDoubleClickEvent(self, e):
        self.doubleClicked.emit()
