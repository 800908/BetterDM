from PyQt5 import QtWidgets, QtCore, QtGui


# ==========START=OF=CLASS====================================

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initUI()

# ---------------------------------------------------

    def initUI(self):
        self.setWindowTitle("Better Download Manager")
        self.setGeometry(50, 100, 640, 480)

        self.initActions()

        self.initMainMenu()

        # self.initToolBar()

        self.statusBar()

        self.initLayoutAndWidget()

# ---------------------------------------------------

    def initActions(self):

        self.action_File_NewDL = mylib.createAction(self, "&New Download", QtGui.QKeySequence.New,
                                                    "To show new download form")

        # ***Batch Download Group Action*****************************
        self.gaction_File_BatchDL = QtWidgets.QActionGroup(self)
        self.action_File_BatchURL = mylib.createAction(
            self, "From &URL ...", "", "Batch downloading from URL")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchURL)
        self.action_File_BatchFile = mylib.createAction(self, "From &File ...", "",
                                                        "Batch downloading from File")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchFile)

        self.action_File_Exit = mylib.createAction(self, "E&xit", "Ctrl+Q",
                                                   "To exit the application", self.close)
        self.action_Download_Start = mylib.createAction(self, "&Start Download", "",
                                                        "To start stoped download")
        self.action_Download_Stop = mylib.createAction(self, "S&top Download", "",
                                                       "To stop started download")
        self.action_Download_Delete = mylib.createAction(self, "&Delete Download", "",
                                                         "To Delete download from list")
        self.action_Help_About = mylib.createAction(self, "&About", "", "To see about window")

# ---------------------------------------------------

    def initMainMenu(self):
        main_Menu = self.menuBar()

        # File menu
        menu_File = main_Menu.addMenu("&File")
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

        # Download menu
        menu_Download = main_Menu.addMenu("&Download")
        # Download --> Start
        menu_Download.addAction(self.action_Download_Start)
        # Download --> Stop
        menu_Download.addAction(self.action_Download_Stop)
        # Download --> Delete
        menu_Download.addAction(self.action_Download_Delete)

        menu_Help = main_Menu.addMenu("&Help")
        # Help --> About menu
        menu_Help.addAction(self.action_Help_About)

# ---------------------------------------------------

    def initToolBar(self):
        main_Toolbar = self.addToolBar("Main Toolbar")

        main_Toolbar.addAction(self.action_File_NewDL)
        main_Toolbar.addAction(self.action_Download_Start)
        main_Toolbar.addAction(self.action_Download_Stop)
        main_Toolbar.addAction(self.action_Download_Delete)


# ---------------------------------------------------

    def initLayoutAndWidget(self):
        splMain = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splLeft = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splRight = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        self.lstwCat = QtWidgets.QListWidget()
        self.toolbDL = QtWidgets.QToolBar("Main Toolbar")
        self.toolbDL.setMaximumHeight(25)
        self.tblwDLs = QtWidgets.QTableWidget()
        self.lstwLog = QtWidgets.QListWidget()

        splLeft.addWidget(self.lstwCat)

        splRight.addWidget(self.toolbDL)
        splRight.addWidget(self.tblwDLs)
        splRight.addWidget(self.lstwLog)
        splRight.setStretchFactor(0, 1)
        splRight.setStretchFactor(1, 6)
        splRight.setStretchFactor(2, 2)

        splMain.addWidget(splLeft)
        splMain.addWidget(splRight)
        splMain.setStretchFactor(0, 1)
        splMain.setStretchFactor(1, 3)

        self.setCentralWidget(splMain)

# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../libs/")
    import mylib

    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    app.exec_()
