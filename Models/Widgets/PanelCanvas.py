from PyQt5.QtCore import Qt, pyqtSignal  # , QByteArray, QBuffer
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QImage

# , QPainterPath
# https://stackoverflow.com/questions/56194201/insert-image-into-qgridlayout-and-draw-on-top-of-image-in-pyqt5


class Canvas(QWidget):

    selected_Color = Qt.red
    released = pyqtSignal(object)

    def __init__(self):
        super(Canvas, self).__init__()
        self.width = 800
        self.height = 500

        self.myPenWidth = 5
        self.myPenColor = Qt.black
        self.image = QImage(self.width, self.height, QImage.Format_ARGB32)
        self.path = QPainterPath()
        self.clearImage()

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
        '''Once the mouse is released, the image will be saved
        and stored into the storyboard'''
        self.saveImage('images.png', "PNG")
        self.released.emit(self.image)

    def sizeHint(self):
        return self.image.size()
