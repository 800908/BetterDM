import sys
from PyQt5 import QtWidgets
from UI.mainwin import MainWindow
from UI.aboutwin import AboutDLG
from libs.mylib import *


def show_aboutme():
    about_win = AboutDLG(main_win)
    about_win.exec_()


app = QtWidgets.QApplication(sys.argv)
main_win = MainWindow()
main_win.action_Help_About.triggered.connect(show_aboutme)
main_win.show()
app.exec_()
