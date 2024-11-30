import sys
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QColor, QPainter, QPixmap
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 302)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 211))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кнопка"))
        self.pushButton.setText(_translate("MainWindow", "НАЖМИ"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = True
        self.pushButton.released.connect(self.run)
        self.window().setFixedSize(self.window().size())

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
            paint.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255), randint(1, 255)))
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