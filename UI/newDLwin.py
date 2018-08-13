from PyQt5 import QtWidgets, QtCore

try:
    from UI.libs import common_func as com_func  # if imported
except ImportError:
    from libs import common_func as com_func  # if run directly

# ==========START=OF=CLASS====================================


class NewDLDLG(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(NewDLDLG, self).__init__(parent)

        self.initUI()
        self.initEventHandlers()
        self.initDefaultVals()

# ---------------------------------------------------

    def initUI(self):

        # ======URL========================================
        self.ledtURL = QtWidgets.QLineEdit("")
        lblURL = com_func.getNewBuddyLabel(u"File &URL:", self.ledtURL)

        # ======Size=======================================
        self.pbtnGetSize = QtWidgets.QPushButton(u"&Get Size")
        lblSize = com_func.getNewBuddyLabel(u"File Size:", self.pbtnGetSize)
        self.lblFileSize = QtWidgets.QLabel("")

        # ======Mirror=====================================
        self.ledtMirror = QtWidgets.QLineEdit("")
        lblMirror = com_func.getNewBuddyLabel(u"&Mirror:", self.ledtMirror)

        # ======File Name==================================
        self.ledtFileName = QtWidgets.QLineEdit("")
        lblFileName = com_func.getNewBuddyLabel(u"&File Name:", self.ledtFileName)

        # ======Folder Name================================
        self.cbSaveFolder = QtWidgets.QComboBox()
        self.tbtnSaveFolder = QtWidgets.QToolButton()
        self.cbSaveFolder.setEditable(True)
        self.cbSaveFolder.addItems(com_func.getValFromAppSettings(
            "NewDL_win/cbSaveFolderItems", [com_func.getSysDLDir()]))

        lblSaveFolder = com_func.getNewBuddyLabel(u"&Save Folder:", self.cbSaveFolder)

        # ======Comment====================================
        self.tedtComment = QtWidgets.QTextEdit("")
        lblComment = com_func.getNewBuddyLabel(u"&Comment:", self.tedtComment)
        self.tedtComment.setMaximumHeight(70)
        self.tedtComment.setAcceptRichText(False)
        lblComment.setAlignment(QtCore.Qt.AlignTop)

        # ======Buttons====================================
        self.pbtnAddStart = QtWidgets.QPushButton(u"&Add Start")
        self.pbtnAddStart.setDefault(True)
        self.pbtnAddPause = QtWidgets.QPushButton(u"Add &Pause")
        self.pbtnCancel = QtWidgets.QPushButton(u"Cancel")
        self.pbtnMoreOp = QtWidgets.QPushButton(u"More &Options")

        hlayButtons = QtWidgets.QHBoxLayout()
        hlayButtons.addWidget(self.pbtnMoreOp)
        hlayButtons.insertSpacing(1, 50)
        hlayButtons.addWidget(self.pbtnCancel)
        hlayButtons.addWidget(self.pbtnAddPause)
        hlayButtons.addWidget(self.pbtnAddStart)

        # ======More Options===============================

        # ------Connections Group--------------------------
        self.spbMaxConn = com_func.getNewSpinBoxwithMinMaxVal(1, 16, 4)
        lblMaxConn = com_func.getNewBuddyLabel(u"Ma&x Connections:", self.spbMaxConn)

        self.spbMaxTry = com_func.getNewSpinBoxwithMinMaxVal(1, 999, 10)
        lblMaxTry = com_func.getNewBuddyLabel(u"Max &Try:", self.spbMaxTry)

        self.spbTryDelay = com_func.getNewSpinBoxwithMinMaxVal(1, 99, 5)
        lblTryDelay = com_func.getNewBuddyLabel(u"Trying &Delay:", self.spbTryDelay)

        glayConn = QtWidgets.QGridLayout()
        glayConn.addWidget(lblMaxConn, 0, 0)
        glayConn.addWidget(self.spbMaxConn, 0, 1)
        glayConn.addWidget(lblMaxTry, 1, 0)
        glayConn.addWidget(self.spbMaxTry, 1, 1)
        glayConn.addWidget(lblTryDelay, 2, 0)
        glayConn.addWidget(self.spbTryDelay, 2, 1)

        gboxConn = QtWidgets.QGroupBox(u"Connections:")
        gboxConn.setLayout(glayConn)

        # ------Identification Group--------------------------
        self.ledtUser = QtWidgets.QLineEdit("")
        lblUserName = com_func.getNewBuddyLabel(u"&User Name:", self.ledtUser)

        self.ledtPass = QtWidgets.QLineEdit("")
        lblPassword = com_func.getNewBuddyLabel(u"&Password:", self.ledtPass)

        glayID = QtWidgets.QGridLayout()
        glayID.addWidget(lblUserName, 0, 0)
        glayID.addWidget(self.ledtUser, 0, 1)
        glayID.addWidget(lblPassword, 1, 0)
        glayID.addWidget(self.ledtPass, 1, 1)

        gboxID = QtWidgets.QGroupBox(u"Identification:")
        gboxID.setLayout(glayID)
        # ----------------------------------------------------
        glayMoreOp = QtWidgets.QGridLayout()
        glayMoreOp.addWidget(gboxConn, 0, 0)
        glayMoreOp.addWidget(gboxID, 0, 1)

        self.frMoreOp = QtWidgets.QFrame()
        self.frMoreOp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMoreOp.hide()
        self.frMoreOp.setLayout(glayMoreOp)

        # ======Main Layout================================
        glayMain = QtWidgets.QGridLayout()

        glayMain.addWidget(lblURL, 0, 0, 1, 2)
        glayMain.addWidget(self.ledtURL, 0, 2, 1, 8)

        glayMain.addWidget(lblSize, 1, 0, 1, 2)
        glayMain.addWidget(self.pbtnGetSize, 1, 2)
        glayMain.addWidget(self.lblFileSize, 1, 3)

        glayMain.addWidget(lblMirror, 2, 0, 1, 2)
        glayMain.addWidget(self.ledtMirror, 2, 2, 1, 8)

        glayMain.addWidget(lblFileName, 3, 0, 1, 2)
        glayMain.addWidget(self.ledtFileName, 3, 2, 1, 8)

        glayMain.addWidget(lblSaveFolder, 4, 0, 1, 2)
        glayMain.addWidget(self.cbSaveFolder, 4, 2, 1, 7)
        glayMain.addWidget(self.tbtnSaveFolder, 4, 9)

        glayMain.addWidget(lblComment, 5, 0, 1, 2)
        glayMain.addWidget(self.tedtComment, 5, 2, 1, 8)

        glayMain.addWidget(com_func.getNewHLine(), 6, 0, 1, 10)

        glayMain.addLayout(hlayButtons, 7, 0, 1, 10)

        glayMain.addWidget(com_func.getNewHLine(), 8, 0, 1, 10)

        glayMain.addWidget(self.frMoreOp, 9, 0, 1, 10)

        glayMain.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.setLayout(glayMain)

# ---------------------------------------------------

    def initDefaultVals(self):
        self.setWindowTitle(u"BDM - New Download")
        self.wantedToAdd = False

        self.ledtURL.setText(com_func.getURLfromClipboard())
        self.ledtFileName.setText(com_func.getFileNamefromURL(self.ledtURL.text()))
        self.on_ledtURL_textChanged()

# ---------------------------------------------------

    def initEventHandlers(self):
        self.ledtURL.textChanged.connect(self.on_ledtURL_textChanged)
        self.ledtURL.editingFinished.connect(self.on_ledURL_editingFinished)

        self.pbtnGetSize.clicked.connect(self.on_pbtnGetSize_clicked)
        self.pbtnAddStart.clicked.connect(self.on_pbtnAddStart_clicked)
        self.pbtnAddPause.clicked.connect(self.on_pbtnAddPause_clicked)
        self.pbtnMoreOp.clicked.connect(self.on_pbtnMoreOp_clicked)
        self.tbtnSaveFolder.clicked.connect(self.on_tbtnSaveFolder_clicked)
        self.pbtnCancel.clicked.connect(self.on_pbtnCancel_clicked)

# ---------------------------------------------------

    def on_ledURL_editingFinished(self):
        if com_func.isItURL(self.ledtURL.text()):
            self.ledtFileName.setText(com_func.getFileNamefromURL(self.ledtURL.text()))

# ---------------------------------------------------

    def on_ledtURL_textChanged(self):
        self.pbtnGetSize.setEnabled(com_func.isItURL(str(self.ledtURL.text())))
        self.pbtnAddStart.setEnabled(self.pbtnGetSize.isEnabled())
        self.pbtnAddPause.setEnabled(self.pbtnGetSize.isEnabled())

# ---------------------------------------------------

    def on_pbtnGetSize_clicked(self):
        if com_func.isItURL(str(self.ledtURL.text())):
            self.lblFileSize.setText(com_func.getReadableFileSize(
                com_func.getSizeOfRemoteFile(str(self.ledtURL.text()))))
        else:
            self.lblFileSize.setText(u"Faild")

# ---------------------------------------------------

    def on_pbtnAddStart_clicked(self):
        if com_func.isItURL(str(self.ledtURL.text())):
            self.wantedToAdd = True
            self.wantedToStart = True
            self.close()
        else:
            com_func.showErrorMessBox(u"Bad URL", u"Please enter correct URL", self)

# ---------------------------------------------------

    def on_pbtnAddPause_clicked(self):
        if com_func.isItURL(str(self.ledtURL.text())):
            self.wantedToAdd = True
            self.wantedToStart = False
            self.close()
        else:
            com_func.showErrorMessBox(u"Bad URL", u"Please enter correct URL", self)

# ---------------------------------------------------

    def on_tbtnSaveFolder_clicked(self):
        fdSaveFolder = QtWidgets.QFileDialog()

        folder2Save = fdSaveFolder.getExistingDirectory(
            self, u"Please choose a folder to save on to",
            self.cbSaveFolder.currentText(),
            QtWidgets.QFileDialog.ShowDirsOnly)

        if folder2Save:
            self.cbSaveFolder.insertItem(0, folder2Save)
            self.cbSaveFolder.setCurrentIndex(0)

# ---------------------------------------------------

    def on_pbtnMoreOp_clicked(self):
        if self.frMoreOp.isVisible():
            self.frMoreOp.hide()
            self.pbtnMoreOp.setText(u"More &Options")
        else:
            self.frMoreOp.show()
            self.pbtnMoreOp.setText(u"Less &Options")
            com_func.moveWindowtoFitDesktop(self)


# ---------------------------------------------------

    def on_pbtnCancel_clicked(self):
        self.close()


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    with open("../rc/appstyle.qss", "rt") as ssFile:
        app.setStyleSheet(ssFile.read())

    newdl_win = NewDLDLG()
    newdl_win.show()
    app.exec_()
