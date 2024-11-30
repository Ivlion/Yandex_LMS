import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QColor, QPainter, QPixmap
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = True
        self.pushButton.released.connect(self.run)

    def run(self):
        self.flag = True

    def paintEvent(self, event):
        if self.pushButton.isDown() and self.flag:
            pixmap = QPixmap(self.label.size())
            pixmap.fill(QColor(0, 0, 0, 0))
            paint = QPainter(pixmap)
            paint.begin(self)
            radius = randint(10, 50)
            center_x = self.label.width() // 2 + randint(-radius, radius)
            center_y = self.label.height() // 2 + randint(-radius, radius)
            paint.setBrush(QColor("yellow"))
            paint.drawEllipse(QPoint(center_x, center_y), radius, radius)
            self.label.setPixmap(pixmap)
            paint.end()
            self.flag = False

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())