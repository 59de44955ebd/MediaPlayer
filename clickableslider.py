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
    def mousePressEvent (self, event):
        sr = self.style().subControlRect(QStyle.CC_Slider, self._opt, QStyle.SC_SliderHandle, self)
        self.is_pressed_outside = event.button() == Qt.LeftButton and not sr.contains(event.pos())
        if self.is_pressed_outside:
            if self.orientation() == Qt.Horizontal:
                newVal = int(self.minimum() + ((self.maximum() - self.minimum()) * (event.x() - self._handle_size // 2)) / (self.width() - self._handle_size))
            else:
                newVal = int(self.maximum() - ((self.maximum() - self.minimum()) * (event.y() - self._handle_size // 2)) / (self.height() - self._handle_size))
            if self.invertedAppearance():
                newVal = self.maximum() - newVal
            self.setValue(newVal)
            self.sliderMoved.emit(newVal)
            event.accept()
        else:
            super().mousePressEvent(event)

    ########################################
    #
    ########################################
    def mouseMoveEvent(self, event):
        if self.is_pressed_outside:
            if self.orientation() == Qt.Horizontal:
                newVal = int(self.minimum() + ((self.maximum() - self.minimum()) * (event.x() - self._handle_size // 2)) / (self.width() - self._handle_size))
            else:
                newVal = int(self.maximum() - ((self.maximum() - self.minimum()) * (event.y() - self._handle_size // 2)) / (self.height() - self._handle_size))
            if self.invertedAppearance():
                newVal = self.maximum() - newVal
            self.setValue(newVal)
            self.sliderMoved.emit(newVal)
            event.accept()
        else:
            super().mouseMoveEvent(event)
