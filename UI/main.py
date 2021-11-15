from PySide2.QtCore import (Qt)
from PySide2.QtWidgets import *

from main_ui import Ui_Form as uimain
from Methods.getInsertedPDF import inserted
import sys
import os
file = sys.argv[0]
dirname = os.path.dirname(file)

class MainWindow(QMainWindow):
    def __init__(self):
        self.cx = 0
        QMainWindow.__init__(self)
        self.ui = uimain()
        self.ui.setupUi(self)

        self.ui.frame.mouseMoveEvent = self.moveWindow
        self.ui.label.mouseMoveEvent = self.moveWindow

        self.show()
        self.ui.pushButton.clicked.connect(self.start)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def start(self):
        items = []
        for x in range(self.ui.listWidget_2.count()):
            items.append(self.ui.listWidget_2.item(x).text())
        print(items)
        if not inserted(items):
            self.ui.listWidget_2.clear()
            self.ui.listWidget_2.addItem("Somethings went wrong")
            self.ui.listWidget_2.addItem("------[Reasons]-------")
            self.ui.listWidget_2.addItem("* file is not decrypted")
            self.ui.listWidget_2.addItem("* file is not found")
            self.ui.listWidget_2.addItem("Exit the program and run it again")
        else:
            self.ui.listWidget_2.addItem("Successful")
            self.ui.listWidget_2.addItem("------")
            self.ui.listWidget_2.addItem("saved to :")
            self.ui.listWidget_2.addItem(dirname + "/../Sources/")
    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
