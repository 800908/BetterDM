from PyQt4 import QtGui, QtCore


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

        # self.initToolBar()

        self.statusBar()

        self.initLayoutAndWidget()

# ---------------------------------------------------

    def initActions(self):

        def createAction(actTitle="New Action", actShortcut="", actTip="", actTriger=None):

            Result = QtGui.QAction(actTitle, self)
            Result.setShortcut(actShortcut)
            Result.setToolTip(actTip)
            Result.setStatusTip(actTip)
            if actTriger:
                Result.triggered.connect(actTriger)

            return Result

        self.action_File_NewDL = createAction("&New Download", QtGui.QKeySequence.New,
                                              "To show new download form")

        # ***Batch Download Group Action*****************************
        self.gaction_File_BatchDL = QtGui.QActionGroup(self)
        self.action_File_BatchURL = createAction("From &URL ...", "", "Batch downloading from URL")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchURL)
        self.action_File_BatchFile = createAction("From &File ...", "",
                                                  "Batch downloading from File")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchFile)

        self.action_File_Exit = createAction("E&xit", "Ctrl+Q", "To exit the application",
                                             self.close)
        self.action_Download_Start = createAction("&Start Download", "",
                                                  "To start stoped download")
        self.action_Download_Stop = createAction("S&top Download", "",
                                                 "To stop started download")
        self.action_Download_Delete = createAction("&Delete Download", "",
                                                   "To Delete download from list")
        self.action_Help_About = createAction("&About", "", "To see about window")

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
        splMain = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splLeft = QtGui.QSplitter(QtCore.Qt.Vertical)
        splRight = QtGui.QSplitter(QtCore.Qt.Vertical)

        self.lstwCat = QtGui.QListWidget()
        self.toolbDL = QtGui.QToolBar("Main Toolbar")
        self.toolbDL.setMaximumHeight(25)
        self.tblwDLs = QtGui.QTableWidget()
        self.lstwLog = QtGui.QListWidget()

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
    app = QtGui.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    app.exec_()
