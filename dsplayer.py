import os

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget

from dshow import Player

# completely optional
SUPPORT_LNK_FILES = True
if SUPPORT_LNK_FILES:
    from lnk import get_lnk_target_path


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
        self._media_loaded = False
        self._muted = False

        # make window background black
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        self._player = Player(
            hwnd=int(self.winId()),
            width=640,
            height=360,
            filter_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources', 'filters')
            )

        self._volume = self._player.get_volume()

    ########################################
    #
    ########################################
    def load_media(self, filename: str):
        if self._media_loaded:
            self.close_media()
        try:
            if SUPPORT_LNK_FILES and filename.lower().endswith('.lnk'):
                filename = get_lnk_target_path(filename)
            ok = self._player.load_file(filename)
            if ok:
                self.play()
                self.pause()
                self.filename = filename
                self._media_loaded = True
        except:
            pass
        self.mediaReady.emit(self._media_loaded)

    ########################################
    #
    ########################################
    def close_media(self):
        if self._media_loaded:
            self._player.close_file()
            self.filename = None
            self._media_loaded = False
            self.repaint()

    ########################################
    #
    ########################################
    def step(self, steps: int=1):
        if self._media_loaded:
            self._player.step(steps)

    ########################################
    #
    ########################################
    def get_natural_size(self):
        if self._media_loaded:
            return self._player.get_size()

    ########################################
    # as seconds (float)
    ########################################
    def get_duration(self):
        try:
            return self._player.get_duration() / 1000
        except:
            return 0

    ########################################
    #
    ########################################
    def get_fps(self):
        if self._media_loaded:
            return self._player.get_fps()

    ########################################
    #
    ########################################
    def has_video(self):
        return self._player.has_video()

    ########################################
    #
    ########################################
    def has_audio(self):
        return self._player.has_audio()

    ########################################
    # 0..1 (float)
    ########################################
    def get_volume(self):
        return self._volume

    ########################################
    # 0..1 (float)
    ########################################
    def set_volume(self, volume: float):
        self._volume = volume
        if not self._muted:
            self._player.set_volume(float(volume))

    ########################################
    #
    ########################################
    def set_muted(self, flag: bool):
        self._muted = flag
        self._player.set_volume(0 if flag else self._volume)

    ########################################
    # as seconds (float)
    ########################################
    def seek_to_time(self, sec: float):
        if self._media_loaded:
            self._player.set_time(sec * 1000)

    ########################################
    # as seconds (float)
    ########################################
    def get_time(self):
        return self._player.get_time() / 1000 if self._media_loaded else 0

    ########################################
    #
    ########################################
    def play(self):
        if self._media_loaded:
            self._player.play()

    ########################################
    #
    ########################################
    def pause(self):
        if self._media_loaded:
            self._player.pause()

    ########################################
    # returns is_playing as bool
    ########################################
    def toggle_playback(self):
        if not self._media_loaded:
            return False
        self._player.toggle_playback()
        return self._player.get_state() == 2

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

	########################################
	#
	########################################
    def resizeEvent(self, event):
        g = self.geometry()
        self._player.resize(g.width(), g.height())
        super().resizeEvent(event)
