from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MySlider(QSlider):

    ########################################
    #
    ########################################
    def mousePressEvent (self, event):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        sr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

        #if event.button() == Qt.LeftButton and not sr.contains(event.pos()):

        self.is_pressed_outside = event.button() == Qt.LeftButton and not sr.contains(event.pos())
        if self.is_pressed_outside:
            if self.orientation() == Qt.Horizontal:
                newVal = int(self.minimum() + ((self.maximum() - self.minimum()) * event.x()) / self.width())
            else:
                newVal = int(self.maximum() - ((self.maximum() - self.minimum()) * event.y()) / self.height())
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
                newVal = int(self.minimum() + ((self.maximum() - self.minimum()) * event.x()) / self.width())
            else:
                newVal = int(self.maximum() - ((self.maximum() - self.minimum()) * event.y()) / self.height())
            if self.invertedAppearance():
                newVal = self.maximum() - newVal
            self.setValue(newVal)
            self.sliderMoved.emit(newVal)
            event.accept()
        else:
            super().mouseMoveEvent(event)
