from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen
# , QPainterPath
# https://stackoverflow.com/questions/56194201/insert-image-into-qgridlayout-and-draw-on-top-of-image-in-pyqt5


class Canvas(QWidget):

    imgFile = 'barn-clipart-vector-25.png'
    selected_Color = Qt.red

    def __init__(self):
        super(Canvas, self).__init__()
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QPixmap(800, 500)  # ("./Models/" + self.imgFile)
        
        self.image.fill(Qt.white)

    def paintEvent(self, event):
        painter = QPainter(self)
        # painter.drawImage(event.rect(), self.image, self.rect())
        painter.drawPixmap(QPoint(), self.image)

    def mousePressEvent(self, event):
        """Controls what happens when a mouse button is pressed"""
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        """Controls what happens when the mouse moves"""
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        """Controls what happens when a mouse button is released"""
        if event.button == Qt.LeftButton:
            self.drawing = False

    def updateImage(self, imgPath):
        self.image = QPixmap(imgPath)

    def sizeHint(self):
        return self.image.size()
