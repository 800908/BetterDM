import sys
from PyQt4 import QtGui
from UI.mainwin import MainWindow
from UI.aboutwin import AboutDLG


def show_aboutme():
    about_win = AboutDLG(main_win)
    about_win.exec_()


app = QtGui.QApplication(sys.argv)
main_win = MainWindow()
main_win.action_Help_About.triggered.connect(show_aboutme)
main_win.show()
app.exec_()
