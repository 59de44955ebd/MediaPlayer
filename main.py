import os
import sys
import traceback

from PyQt5.QtCore import Qt, QResource, QTimer, QTime, QEvent, pyqtSignal
from PyQt5.QtWidgets import (qApp, QMainWindow, QApplication, QWidget, QToolButton, QSlider, QLabel,
        QSizePolicy, QActionGroup, QMessageBox, QFileDialog)
from PyQt5 import uic

from dark import palette
from clickableslider import ClickableSlider

APP_NAME = 'MediaPlayer'
APP_VERSION = '0.4'

IS_WIN = sys.platform == 'win32'
IS_MAC = sys.platform == 'darwin'
if not IS_WIN and not IS_MAC:
    sys.exit(1)

IS_FROZEN = getattr(sys, 'frozen', False)
if IS_FROZEN:
    if IS_WIN:
        RES_DIR = os.path.join(os.path.dirname(sys.executable), '_internal', 'resources')
    else:
        RES_DIR = os.path.join(os.path.dirname(sys.executable), '..', 'Resources')
else:
    RES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')

if IS_WIN:
    from ctypes import windll, c_int, byref
    from ctypes.wintypes import HWND, DWORD, LPCVOID

    windll.dwmapi.DwmSetWindowAttribute.argtypes = (HWND, DWORD, LPCVOID, DWORD)
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20

TIME_DISPLAY_UPDATE_PERIOD = 250


class Main(QMainWindow):

    ########################################
    #
    ########################################
    def __init__(self, app):
        super().__init__()

        if IS_MAC and IS_FROZEN:
            app.fileOpened.connect(lambda filename:
                    self.video_widget.load_media(filename))
        self._duration = 0
        self._duration_str = ''
        self._time_format = 'hh:mm:ss'
        self._show_msec = False
        self._fullscreen = False

        if IS_WIN:
            windll.dwmapi.DwmSetWindowAttribute(int(self.winId()),
                    DWMWA_USE_IMMERSIVE_DARK_MODE, byref(c_int(1)), 4)

        QApplication.setStyle('Fusion')
        qApp.setPalette(palette)
        with open(os.path.join(RES_DIR, 'style.css'), 'r') as f:
            qApp.setStyleSheet(f.read())

        QResource.registerResource(os.path.join(RES_DIR, 'main.rcc'))
        uic.loadUi(os.path.join(RES_DIR, 'main.ui'), self)

        # menu
        self.action_open.triggered.connect(self.slot_open)
        self.action_close.triggered.connect(lambda:
            self.video_widget.close_media() or self.slot_ready(False))
        self.action_toggle_fullscreen.triggered.connect(self.slot_toggle_fullscreen)
        self.action_toggle_show_msecs.triggered.connect(self.slot_toggle_show_msecs)
        self.action_toggle_play.triggered.connect(self.slot_toggle_playback)
        self.action_step_forward.triggered.connect(lambda: self.video_widget.step(1))
        self.action_step_back.triggered.connect(lambda: self.video_widget.step(-1))
        self.action_skip_forward.triggered.connect(lambda:
            self.video_widget.seek_to_time(self.video_widget.get_time() + 1))
        self.action_skip_back.triggered.connect(lambda:
            self.video_widget.seek_to_time(self.video_widget.get_time() - 1))
        self.action_volume_up.triggered.connect(lambda:
            self.slider_volume.setValue(self.slider_volume.value() + 1))
        self.action_volume_down.triggered.connect(lambda:
            self.slider_volume.setValue(self.slider_volume.value() - 1))
        self.action_toggle_mute.toggled.connect(self.video_widget.set_muted)
        self.action_about.triggered.connect(self.slot_about)

        # statusbar
        self.label_statusbar = QLabel()
        self.label_statusbar.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.statusbar.addPermanentWidget(self.label_statusbar)

        # toolbar
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolBar.addWidget(spacer)
        self.toolBar.addAction(self.action_toggle_mute)
        self.slider_volume = ClickableSlider(Qt.Horizontal)
        self.slider_volume.setFixedWidth(100)
        self.slider_volume.setRange(0, 100)
        self.slider_volume.valueChanged.connect(lambda value:
                self.video_widget.set_volume(value / 100))
        self.toolBar.addWidget(self.slider_volume)

        ag = QActionGroup(self)
        ag.addAction(self.action_play)
        ag.addAction(self.action_pause)
        ag.addAction(self.action_stop)

        self.action_play.triggered.connect(self.video_widget.play)
        self.action_pause.triggered.connect(self.video_widget.pause)
        self.action_stop.triggered.connect(lambda:
            self.video_widget.pause() or self.video_widget.seek_to_time(0))

        self.video_widget.mediaReady.connect(self.slot_ready)
        self.video_widget.mousePressed.connect(self.slot_toggle_playback)
        self.video_widget.doubleClicked.connect(self.slot_double_clicked)

        self.slider_time.sliderMoved.connect(lambda value:
                self.video_widget.seek_to_time(value / 10000 * self._duration) if self._duration else None)

        self._timer = QTimer(self)
        self._timer.setInterval(TIME_DISPLAY_UPDATE_PERIOD)
        self._timer.timeout.connect(self.slot_update_time)

        self.slider_volume.setValue(int(100 * self.video_widget.get_volume()))

        if len(sys.argv) > 1:
            self.video_widget.load_media(sys.argv[1])

        self.show()

        self.setMinimumHeight(self.height() - self.video_widget.height())

    ########################################
    #
    ########################################
    def closeEvent(self, e):
        super().closeEvent(e)
        sys.exit(0)  # needed for macOS only

    ########################################
    #
    ########################################
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()

    ########################################
    #
    ########################################
    def dropEvent(self, e):
        self.video_widget.load_media(e.mimeData().urls()[0].toLocalFile())

    ########################################
    #
    ########################################
    def slot_ready(self, ok):
        self.slider_time.setValue(0)
        if ok:
            has_video = self.video_widget.has_video()
            if has_video:
                w, h = self.video_widget.get_natural_size()
                dh = self.height() - self.video_widget.height()
                self.resize(int(w), int(h) + dh)  # resize window to video
            self._duration = self.video_widget.get_duration()
            if self._duration > 0:
                self._time_format = ('hh:mm:ss' if self._duration >= 3600 else 'mm:ss') + ('.zzz' if self._show_msec else '')
                self._duration_str = ' / ' + QTime(0, 0).addMSecs(int(1000 * self._duration)).toString(self._time_format)
            else:
                self._time_format = 'hh:mm:ss' + ('.zzz' if self._show_msec else '')
            self.slider_time.setEnabled(self._duration > 0)
            self.label_statusbar.setVisible(True) #self._duration > 0)
            self.action_toggle_fullscreen.setEnabled(has_video)
            self.action_toggle_play.setEnabled(True)
            for action in (self.action_play, self.action_pause, self.action_stop):
                action.setEnabled(True)
            for action in (self.action_skip_back, self.action_step_back, self.action_step_forward, self.action_skip_forward):
                action.setEnabled(self._duration > 0)
            self._timer.start()
            self.video_widget.play()
            self.action_play.setChecked(True)
            self.setWindowTitle(f'{os.path.basename(self.video_widget.filename)} - {APP_NAME}')
        else:
            self._timer.stop()
            self.slider_time.setEnabled(False)
            self.label_statusbar.setVisible(False)
            self.action_toggle_fullscreen.setEnabled(False)
            self.action_toggle_play.setEnabled(False)
            for action in (self.action_play, self.action_pause, self.action_stop, self.action_skip_back,
                    self.action_step_back, self.action_step_forward, self.action_skip_forward):
                action.setEnabled(False)
            self.action_stop.setChecked(True)
            self.setWindowTitle(APP_NAME)

    ########################################
    #
    ########################################
    def slot_open(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Select media file')
        if filename:
            self.video_widget.load_media(filename)

    ########################################
    #
    ########################################
    def slot_about(self):
        msg = ('<b>{} v{}</b><br>(c) 2024 59de44955ebd<br><br>'
            'A simple media player for macOS and Windows, based on '
            'Python 3, PyQt5 and native system media frameworks '
            '(AVFoundation/DirectShow).<br>').format(APP_NAME, APP_VERSION)
        dialog = QMessageBox(QMessageBox.Information, 'About', msg, QMessageBox.Ok, parent=self)
        if IS_WIN:
            windll.dwmapi.DwmSetWindowAttribute(int(dialog.winId()),
                    DWMWA_USE_IMMERSIVE_DARK_MODE, byref(c_int(1)), 4)
        dialog.exec()

    ########################################
    #
    ########################################
    def slot_update_time(self):
        if self._duration > 0:
            self.slider_time.setValue(int(10000 * self.video_widget.get_time() / self._duration))
            self.label_statusbar.setText(QTime(0, 0).addMSecs(int(1000 * self.video_widget.get_time())).toString(self._time_format) + self._duration_str)
        else:
            self.label_statusbar.setText(QTime(0, 0).addMSecs(int(1000 * self.video_widget.get_time())).toString(self._time_format))

    ########################################
    #
    ########################################
    def slot_toggle_playback(self):
        state = self.video_widget.toggle_playback()
        if state is None:
            return
        if state == 1:
            self.action_play.setChecked(True)
        else:
            self.action_pause.setChecked(True)

    ########################################
    #
    ########################################
    def slot_toggle_fullscreen(self):
        if not self.video_widget.has_video():
            return
        self._fullscreen = not self._fullscreen
        if self._fullscreen:
            self.video_widget.setParent(None)
            self.video_widget.showFullScreen()
        else:
            self.video_widget.showNormal()
            self.centralwidget.layout().insertWidget(0, self.video_widget)

    ########################################
    #
    ########################################
    def slot_toggle_show_msecs(self, flag):
        self._show_msec = flag
        if self._duration > 0:
            self._time_format = ('hh:mm:ss' if self._duration >= 3600 else 'mm:ss') + ('.zzz' if self._show_msec else '')
            self._duration_str = ' / ' + QTime(0, 0).addMSecs(int(1000 * self._duration)).toString(self._time_format)
        else:
            self._time_format = 'hh:mm:ss' + ('.zzz' if self._show_msec else '')

    ########################################
    #
    ########################################
    def slot_double_clicked(self):
        self.video_widget.toggle_playback()
        self.slot_toggle_fullscreen()


if __name__ == '__main__':
    sys.excepthook = traceback.print_exception
    if IS_MAC and IS_FROZEN:
        class MyApplication(QApplication):
            fileOpened = pyqtSignal(str)
            def event(self, e):
                if e.type() == QEvent.FileOpen:
                    self.fileOpened.emit(e.file())
                return super().event(e)
        app = MyApplication(sys.argv)
    else:
        app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus)
    main = Main(app)
    sys.exit(app.exec_())
