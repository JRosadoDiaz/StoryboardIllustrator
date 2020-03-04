from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QImage
# , QPainterPath
# https://stackoverflow.com/questions/56194201/insert-image-into-qgridlayout-and-draw-on-top-of-image-in-pyqt5


class Canvas(QWidget):

    # imgFile = 'barn-clipart-vector-25.png'
    selected_Color = Qt.red
    released = pyqtSignal(object)

    def __init__(self):
        super(Canvas, self).__init__()

        w = 800
        h = 500

        self.myPenWidth = 13
        self.myPenColor = Qt.black
        self.image = QImage(w, h, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.clearImage()
        # self.image = QPixmap("./Models/" + self.imgFile)

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.update()

    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        """Controls what happens when the mouse moves"""
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,
                      self.myPenWidth, Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        self.update()

    def mouseReleaseEvent(self, event):
        self.released.emit(self.image)
        self.saveImage('images.png', "PNG")

    def sizeHint(self):
        return self.image.size()
