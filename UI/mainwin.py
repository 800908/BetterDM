from PyQt5 import QtWidgets, QtCore, QtGui

try:
    from UI.libs import common_func as com_func  # if imported
except ImportError:
    from libs import common_func as com_func  # if run directly


# ==========START=OF=CLASS====================================

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.initDefaultVals()
        self.initUI()

# ************************************************************************

    def initUI(self):

        self.initActions()

        self.initMainMenu()

        self.initToolBar()

        self.statusBar()

        self.initLayoutAndWidget()

        self.initWindowSizeAndPos()

        self.initEventHandlers()

# ************************************************************************

    def initDefaultVals(self):
        self.setWindowTitle("Better Download Manager")
        self.Settings = com_func.getAppSettings()


# ************************************************************************

    def saveWindowSettings(self):
        if self.isMaximized():
            self.Settings.setValue("Main_win/iswinmaximized", True)
        else:
            self.Settings.setValue("Main_win/iswinmaximized", False)
            self.Settings.setValue("Main_win/win_width", self.width())
            self.Settings.setValue("Main_win/win_height", self.height())
            self.Settings.setValue("Main_win/win_xpos", self.x())
            self.Settings.setValue("Main_win/win_ypos", self.y())

        for col_num in range(self.tblwDLs.columnCount()):
            self.Settings.setValue("Main_win/table_col{}_width".format(col_num),
                                   self.tblwDLs.columnWidth(col_num))

        self.Settings.setValue("Main_win/Main_spliter_state", self.splMain.saveState())
        self.Settings.setValue("Main_win/Right_spliter_state", self.splRight.saveState())
        self.Settings.setValue("Main_win/Left_spliter_state", self.splLeft.saveState())

        for col_num in range(2):
            self.Settings.setValue("Main_win/FileTree_col{}_width".format(col_num),
                                   self.trvFiles.columnWidth(col_num))

# ************************************************************************

    def closeEvent(self, event):
        self.saveWindowSettings()
        event.accept()

# ************************************************************************

    def initEventHandlers(self):
        pass


# ************************************************************************

    def initWindowSizeAndPos(self):
        isWinMaximized = self.Settings.value("Main_win/iswinmaximized", True, bool)

        if isWinMaximized:
            self.showMaximized()
        else:
            win_width = self.Settings.value("Main_win/win_width", 640, int)
            win_height = self.Settings.value("Main_win/win_height", 480, int)
            win_xpos = self.Settings.value("Main_win/win_xpos", 50, int)
            win_ypos = self.Settings.value("Main_win/win_ypos", 50, int)

            self.resize(win_width, win_height)
            self.move(win_xpos, win_ypos)

# ************************************************************************

    def initActions(self):

        self.action_File_NewDL = com_func.getNewAction(
            self, "&New Download", QtGui.QKeySequence.New, "To show new download form")

        # ---Batch Download Group Action---------------------------------
        self.gaction_File_BatchDL = QtWidgets.QActionGroup(self)
        self.action_File_BatchURL = com_func.getNewAction(
            self, "From &URL ...", "", "Batch downloading from URL")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchURL)
        self.action_File_BatchFile = com_func.getNewAction(
            self, "From &File ...", "", "Batch downloading from File")
        self.gaction_File_BatchDL.addAction(self.action_File_BatchFile)

        self.action_File_Exit = com_func.getNewAction(
            self, "E&xit", "Ctrl+Q", "To exit the application", self.close)
        self.action_Download_Start = com_func.getNewAction(
            self, "&Start Download", "", "To start stoped download")
        self.action_Download_Stop = com_func.getNewAction(
            self, "S&top Download", "", "To stop started download")
        self.action_Download_Delete = com_func.getNewAction(
            self, "&Delete Download", "", "To Delete download from list")
        self.action_Help_About = com_func.getNewAction(self, "&About", "", "To see about window")

# ************************************************************************

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

# ************************************************************************

    def initToolBar(self):
        main_Toolbar = self.addToolBar("Main Toolbar")

        main_Toolbar.addAction(self.action_File_NewDL)
        main_Toolbar.addAction(self.action_Download_Start)
        main_Toolbar.addAction(self.action_Download_Stop)
        main_Toolbar.addAction(self.action_Download_Delete)


# ************************************************************************

    def initLayoutAndWidget(self):
        self.splMain = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splLeft = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.splRight = QtWidgets.QSplitter(QtCore.Qt.Vertical)

    # -----------------------------------------------------
        # self.toolbDL = QtWidgets.QToolBar("Main Toolbar")
        # self.toolbDL.setMaximumHeight(25)

    # -----------------------------------------------------

        self.tblwDLs = QtWidgets.QTableWidget(0, 5)
        self.tblwDLs.setHorizontalHeaderLabels(["File Name", "Size", "Progress",
                                                "DL Speed", "Time to Finish"])
        self.tblwDLs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tblwDLs.setColumnWidth(0, self.Settings.value("Main_win/table_col0_width", 250, int))
        self.tblwDLs.setColumnWidth(1, self.Settings.value("Main_win/table_col1_width", 70, int))
        self.tblwDLs.setColumnWidth(2, self.Settings.value("Main_win/table_col2_width", 150, int))
        self.tblwDLs.setColumnWidth(3, self.Settings.value("Main_win/table_col3_width", 70, int))
        self.tblwDLs.setColumnWidth(4, self.Settings.value("Main_win/table_col4_width", 100, int))

    # -----------------------------------------------------

        self.tedtDLInfo = QtWidgets.QTextEdit()
        # self.tedtDLInfo.setReadOnly(True)
        self.tedtDLInfo.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)

    # -----------------------------------------------------

        self.trwCats = QtWidgets.QTreeWidget()
        self.trwCats.setColumnCount(1)
        self.trwCats.setHeaderLabel("Categories")

        self.trwiDLStatus = com_func.getNewTreeItem("Download Status", self.trwCats)

        self.trwiDLStatus_All = com_func.getNewTreeItem("All", self.trwiDLStatus)
        self.trwiDLStatus_Active = com_func.getNewTreeItem("Active", self.trwiDLStatus)
        self.trwiDLStatus_Finished = com_func.getNewTreeItem("Finished", self.trwiDLStatus)
        self.trwiDLStatus_Stoped = com_func.getNewTreeItem("Stoped", self.trwiDLStatus)
        self.trwiDLStatus_Deleted = com_func.getNewTreeItem("Deleted", self.trwiDLStatus)

        self.trwiFileTypes = com_func.getNewTreeItem("File Types", self.trwCats)

        self.trwiFileTypes_Music = com_func.getNewTreeItem("Muisc", self.trwiFileTypes)
        self.trwiFileTypes_Video = com_func.getNewTreeItem("Video", self.trwiFileTypes)
        self.trwiFileTypes_App = com_func.getNewTreeItem("Application", self.trwiFileTypes)

        self.trwiUserCats = com_func.getNewTreeItem("User Categories", self.trwCats)

        self.trwCats.expandAll()
        self.trwCats.setCurrentItem(self.trwiDLStatus_All)

        self.splLeft.addWidget(self.trwCats)

    # -----------------------------------------------------

        self.trvFiles = QtWidgets.QTreeView()

        self.fsmFiles = QtWidgets.QFileSystemModel()
        self.trvFiles.setModel(self.fsmFiles)

        for i in range(2, self.trvFiles.header().count()):
            self.trvFiles.hideColumn(i)

        self.trvFiles.setColumnWidth(0, self.Settings.value(
            "Main_win/FileTree_col0_width", 150, int))
        self.trvFiles.setColumnWidth(1, self.Settings.value(
            "Main_win/FileTree_col1_width", 50, int))

        self.splLeft.addWidget(self.trvFiles)

    # -----------------------------------------------------

        self.splRight.setStretchFactor(0, 1)
        self.splRight.setStretchFactor(1, 1)

    # -----------------------------------------------------

        # self.splRight.addWidget(self.toolbDL)
        self.splRight.addWidget(self.tblwDLs)
        self.splRight.addWidget(self.tedtDLInfo)
        self.splRight.setStretchFactor(0, 2)
        self.splRight.setStretchFactor(1, 1)

    # -----------------------------------------------------

        self.splMain.addWidget(self.splLeft)
        self.splMain.addWidget(self.splRight)
        self.splMain.setStretchFactor(0, 1)
        self.splMain.setStretchFactor(1, 3)

    # -----------------------------------------------------

        self.setCentralWidget(self.splMain)

    # -----------------------------------------------------

        if self.Settings.contains("Main_win/Main_spliter_state"):
            self.splMain.restoreState(self.Settings.value("Main_win/Main_spliter_state"))

        if self.Settings.contains("Main_win/Right_spliter_state"):
            self.splRight.restoreState(self.Settings.value("Main_win/Right_spliter_state"))

        if self.Settings.contains("Main_win/Left_spliter_state"):
            self.splLeft.restoreState(self.Settings.value("Main_win/Left_spliter_state"))

# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    app.exec_()
