from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QLineEdit,QMessageBox
from PyQt5 import QtGui
import sys
import random_pass as rp
import logging

logging.basicConfig(filename="password.txt",format="%(message)s",level=logging.INFO)

with open("showMessage","r") as f:
    showM = f.read()
    if showM == "1":
        showM = True

    else:
        showM = False


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 500
        self.y = 500
        self.title = "password-getn"
    def start(self):
        self.setGeometry(100,100,self.x,self.y)
        self.setWindowTitle(self.title)
        self.setFixedSize(self.x,self.y)
        self.setWindowIcon(QtGui,Qlcon("lock.png"))

        self.label1 = QLabel(self)
        self.label1.setText("Characters:")
        self.label1.move(190,50)

        self.charsInput = QLineEdit(self)
        self.charsInput.setText("a,b,c,d")
        self.charsInput.setGeometry(190,100,100,30)
        self.label2 = QLabel(self)
