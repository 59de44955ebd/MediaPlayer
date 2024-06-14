import os

from dshow import Player

from PyQt5.QtCore import Qt, pyqtSignal
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
        self._media_loaded = False

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

    ########################################
    #
    ########################################
    def load_media(self, filename: str):
        if self._media_loaded:
            self.close_media()
        try:
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
    # as seconds
    ########################################
    def get_duration(self):
        return self._player.get_duration() / 1000

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
    # 0..1
    ########################################
    def get_volume(self):
        return self._player.get_volume()

    ########################################
    # 0..1
    ########################################
    def set_volume(self, volume: float):
        self._player.set_volume(float(volume))

    ########################################
    #
    ########################################
    def seek_to_time(self, sec: float):
        if self._media_loaded:
            self._player.set_time(sec * 1000)

    ########################################
    # as seconds
    ########################################
    def get_time(self):
        return self._player.get_time() / 1000 if self._media_loaded else 0

    ########################################
    # NEW
    ########################################
    def play(self):
        if self._media_loaded:
            self._player.play()

    ########################################
    # NEW
    ########################################
    def pause(self):
        if self._media_loaded:
            self._player.pause()

    ########################################
    # NEW
    ########################################
    def toggle_playback(self):
        if self._media_loaded:
            self._player.toggle_playback()
            return self._player.get_state() - 1

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