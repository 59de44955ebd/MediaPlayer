'''
Implemenst a slider that "jumps" to the corresponding position if clicked outside the knob,
and then follows the mouse while the left mouse button is pressed.
'''

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QStyleOptionSlider, QStyle


class ClickableSlider(QSlider):

    ########################################
    #
    ########################################
    def __init__(self, *args):
        super().__init__(*args)
        self._opt = QStyleOptionSlider()
        self.initStyleOption(self._opt)
        sr = self.style().subControlRect(QStyle.CC_Slider, self._opt, QStyle.SC_SliderHandle, self)
        self._handle_size = sr.width() if self.orientation() == Qt.Horizontal else sr.height()

    ########################################
    #
    ########################################
    def __set(self, event):
        maxi, mini = self.maximum(), self.minimum()
        if self.orientation() == Qt.Horizontal:
            val = min(maxi, max(mini, int(mini + ((maxi - mini) * (event.x() - self._handle_size // 2)) / (self.width() - self._handle_size))))
        else:
            val = min(maxi, max(mini, int(maxi - ((maxi - mini) * (event.y() - self._handle_size // 2)) / (self.height() - self._handle_size))))
        if self.invertedAppearance():
            val = maxi - val
        self.setValue(val)
        self.sliderMoved.emit(val)
        event.accept()

    ########################################
    #
    ########################################
    def mousePressEvent (self, event):
        sr = self.style().subControlRect(QStyle.CC_Slider, self._opt, QStyle.SC_SliderHandle, self)
        self.is_pressed_outside = event.button() == Qt.LeftButton and not sr.contains(event.pos())
        if self.is_pressed_outside:
            self.__set(event)
        else:
            super().mousePressEvent(event)

    ########################################
    #
    ########################################
    def mouseMoveEvent(self, event):
        if self.is_pressed_outside:
            self.__set(event)
        else:
            super().mouseMoveEvent(event)
