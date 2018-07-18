import sys
from PyQt4 import QtGui


# ==========START=OF=CLASS====================================

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initUI()

# ---------------------------------------------------

    def initUI(self):
        self.setWindowTitle("Better Download Manager")
        self.setGeometry(50, 100, 640, 480)

        self.initActions()

        self.initMainMenu()

        self.statusBar()

# ---------------------------------------------------

    def initActions(self):

        # ***New Download Action*************************************
        self.action_File_NewDL = QtGui.QAction("&New Download", self)
        self.action_File_NewDL.setShortcut(QtGui.QKeySequence.New)
        self.action_File_NewDL.setToolTip("To show new download form")
        self.action_File_NewDL.setStatusTip("To show new download form")
        # action_File_NewDL.triggered.connect(self.shownewdlform)

        # # ***Batch Download Action***********************************
        # self.action_File_NewBatchDL = QtGui.QAction("&Batch Download", self)
        # self.action_File_NewBatchDL.setToolTip("For batch downloading")
        # self.action_File_NewBatchDL.setStatusTip("For batch downloading")

        # ***Batch Download Group Action*****************************
        self.gaction_File_BatchDL = QtGui.QActionGroup(self)
        # Batch Download from URL Action
        self.action_File_BatchURL = QtGui.QAction("From &URL ...", self)
        self.action_File_BatchURL.setToolTip("Batch downloading from URL")
        self.action_File_BatchURL.setStatusTip("Batch downloading from URL")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchURL)
        # Batch Download from File Action
        self.action_File_BatchFile = QtGui.QAction("From &File ...", self)
        self.action_File_BatchFile.setToolTip("Batch downloading from File")
        self.action_File_BatchFile.setStatusTip("Batch downloading from File")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchFile)

        # ***Exit Action*********************************************
        self.action_File_Exit = QtGui.QAction("E&xit", self)
        self.action_File_Exit.setShortcut("Ctrl+Q")
        self.action_File_Exit.setToolTip("To exit the application")
        self.action_File_Exit.setStatusTip("To exit the application")
        self.action_File_Exit.triggered.connect(self.close)

        # ***About Action********************************************
        self.action_Help_About = QtGui.QAction("&About", self)
        self.action_Help_About.setToolTip("To see about window")
        self.action_Help_About.setStatusTip("To see about window")
        # action_Help_About.triggered.connect(self.showaboutwin)

# ---------------------------------------------------

    def initMainMenu(self):
        main_menu = self.menuBar()

        # File menu
        menu_File = main_menu.addMenu("&File")
        # File --> New Download
        menu_File.addAction(self.action_File_NewDL)
        # File --> Batch Download submenu
        submenu_File_BatchDL = menu_File.addMenu("&Batch Download")
        submenu_File_BatchDL.addAction(self.action_File_BatchURL)
        submenu_File_BatchDL.addAction(self.action_File_BatchFile)
        menu_File.addMenu(submenu_File_BatchDL)

        # File --> Separator
        menu_File.addSeparator()

        # File --> Exit menu
        menu_File.addAction(self.action_File_Exit)

        menu_Download = main_menu.addMenu("&Download")

        menu_Help = main_menu.addMenu("&Help")
        # Help --> About menu
        menu_Help.addAction(self.action_Help_About)

# ============END=OF=CLASS====================================


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    main_win = MainWindow()
    main_win.show()

    app.exec_()
