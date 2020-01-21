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
        self.image = QPixmap("./Models/" + self.imgFile)
        print("Canvas has been created")

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def sizeHint(self):
        return self.image.size()
