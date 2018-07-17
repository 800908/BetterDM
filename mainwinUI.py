import sys
from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Better Download Manager")
        self.setGeometry(50, 100, 800, 600)

        File_Exit = QtGui.QAction("E&xit", self)
        File_Exit.setShortcut("Ctrl+Q")
        File_Exit.setStatusTip("Exit the application")
        File_Exit.triggered.connect(self.close)

        self.statusBar()
        main_menu = self.menuBar()
        sub_File_menu = main_menu.addMenu("&File")
        sub_File_menu.addAction(File_Exit)


def runApp():
    app = QtGui.QApplication(sys.argv)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    runApp()
