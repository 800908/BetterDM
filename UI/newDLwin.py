from PyQt4 import QtGui, QtCore


# ==========START=OF=CLASS====================================


class NewDLDLG(QtGui.QDialog):

    def __init__(self, parent=None):
        super(NewDLDLG, self).__init__(parent)

        self.initUI()
        self.initEventHandlers()

# ---------------------------------------------------

    def initUI(self):
        self.setWindowTitle(u"BDM - New Download")
        self.setMinimumSize(450, 200)

        # ======URL========================================
        lblURL = QtGui.QLabel(u"File &URL:")
        self.ledtURL = QtGui.QLineEdit("")
        lblURL.setBuddy(self.ledtURL)
        # lblURL.setAlignment(QtCore.Qt.AlignRight)

        # ======Size=======================================
        lblSize = QtGui.QLabel(u"File Size:")
        self.lblFileSize = QtGui.QLabel("")
        self.pbtnGetSize = QtGui.QPushButton(u"&Get Size")
        lblSize.setBuddy(self.lblFileSize)
        # lblSize.setAlignment(QtCore.Qt.AlignRight)

        # ======Mirror=====================================
        lblMirror = QtGui.QLabel(u"&Mirror:")
        self.ledtMirror = QtGui.QLineEdit("")
        lblMirror.setBuddy(self.ledtMirror)
        # lblMirror.setAlignment(QtCore.Qt.AlignRight)

        # ======File Name==================================
        lblFileName = QtGui.QLabel(u"&File Name:")
        self.ledtFileName = QtGui.QLineEdit("")
        lblFileName.setBuddy(self.ledtFileName)
        # lblFileName.setAlignment(QtCore.Qt.AlignRight)

        # ======Folder Name================================
        lblSaveFolder = QtGui.QLabel(u"&Save Folder:")
        self.cbSaveFolder = QtGui.QComboBox()
        self.tbtnSaveFolder = QtGui.QToolButton()
        self.cbSaveFolder.setEditable(True)
        lblSaveFolder.setBuddy(self.cbSaveFolder)
        # lblSaveFolder.setAlignment(QtCore.Qt.AlignRight)

        # ======Comment====================================
        lblComment = QtGui.QLabel(u"&Comment:")
        self.tedtComment = QtGui.QTextEdit("")
        lblComment.setBuddy(self.tedtComment)
        self.tedtComment.setMaximumHeight(70)
        lblComment.setAlignment(QtCore.Qt.AlignTop)

        # ======More Options===============================

        # ------Connections Group--------------------------
        lblMaxConn = QtGui.QLabel(u"Ma&x Connections:")
        self.spbMaxConn = QtGui.QSpinBox()
        self.spbMaxConn.setValue(4)
        self.spbMaxConn.setMinimum(1)
        self.spbMaxConn.setMaximum(16)
        lblMaxConn.setBuddy(self.spbMaxConn)

        lblMaxTry = QtGui.QLabel(u"Max &Try:")
        self.spbMaxTry = QtGui.QSpinBox()
        self.spbMaxTry.setValue(10)
        self.spbMaxTry.setMinimum(1)
        self.spbMaxTry.setMaximum(999)
        lblMaxTry.setBuddy(self.spbMaxTry)

        lblTryDelay = QtGui.QLabel(u"Trying &Delay:")
        self.spbTryDelay = QtGui.QSpinBox()
        self.spbTryDelay.setValue(5)
        self.spbTryDelay.setMinimum(1)
        self.spbTryDelay.setMaximum(99)
        lblTryDelay.setBuddy(self.spbTryDelay)

        glayConn = QtGui.QGridLayout()
        glayConn.addWidget(lblMaxConn, 0, 0)
        glayConn.addWidget(self.spbMaxConn, 0, 1)
        glayConn.addWidget(lblMaxTry, 1, 0)
        glayConn.addWidget(self.spbMaxTry, 1, 1)
        glayConn.addWidget(lblTryDelay, 2, 0)
        glayConn.addWidget(self.spbTryDelay, 2, 1)

        gboxConn = QtGui.QGroupBox(u"Connections:")
        gboxConn.setLayout(glayConn)

        # ------Identification Group--------------------------
        lblUserName = QtGui.QLabel(u"&User Name:")
        self.ledtUser = QtGui.QLineEdit("")
        lblUserName.setBuddy(self.ledtUser)

        lblPassword = QtGui.QLabel(u"&Password:")
        self.ledtPass = QtGui.QLineEdit("")
        lblPassword.setBuddy(self.ledtPass)

        glayID = QtGui.QGridLayout()
        glayID.addWidget(lblUserName, 0, 0)
        glayID.addWidget(self.ledtUser, 0, 1)
        glayID.addWidget(lblPassword, 1, 0)
        glayID.addWidget(self.ledtPass, 1, 1)

        gboxID = QtGui.QGroupBox(u"Identification:")
        gboxID.setLayout(glayID)
        # ----------------------------------------------------
        glayMoreOp = QtGui.QGridLayout()
        glayMoreOp.addWidget(gboxConn, 0, 0)
        glayMoreOp.addWidget(gboxID, 0, 1)

        self.frMoreOp = QtGui.QFrame()
        self.frMoreOp.setLayout(glayMoreOp)
        self.frMoreOp.setFrameShape(QtGui.QFrame.NoFrame)
        self.frMoreOp.hide()

        # ======Bottom Line================================
        frBottomLine = QtGui.QFrame()
        frBottomLine.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Sunken)

        # ======Buttons====================================
        self.pbtnAdd_Start = QtGui.QPushButton(u"&Add Start")
        self.pbtnAdd_Pause = QtGui.QPushButton(u"Add &Pause")
        self.pbtnCancel = QtGui.QPushButton(u"Cancel")
        self.pbtnMoreOp = QtGui.QPushButton(u"More &Options")
        # self.pbtnMoreOp.setCheckable(True)

        hlayButtons = QtGui.QHBoxLayout()
        hlayButtons.addWidget(self.pbtnMoreOp)
        hlayButtons.insertSpacing(1, 50)
        hlayButtons.addWidget(self.pbtnCancel)
        hlayButtons.addWidget(self.pbtnAdd_Pause)
        hlayButtons.addWidget(self.pbtnAdd_Start)

        # ======Main Layout================================
        glayMain = QtGui.QGridLayout()

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

        glayMain.addWidget(self.frMoreOp, 6, 0, 1, 10)

        glayMain.addWidget(frBottomLine, 7, 0, 1, 10)

        glayMain.addLayout(hlayButtons, 8, 0, 1, 10)

        glayMain.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.setLayout(glayMain)

# ---------------------------------------------------

    def initEventHandlers(self):
        self.pbtnMoreOp.clicked.connect(self.show_hide_OP)
        self.tbtnSaveFolder.clicked.connect(self.setFolder2Save)

# ---------------------------------------------------
    def setFolder2Save(self):
        fdSaveFolder = QtGui.QFileDialog()

        folder2Save = fdSaveFolder.getExistingDirectory(self,
                                                        u"Please choose a folder to save on",
                                                        QtCore.QDir.homePath(),
                                                        QtGui.QFileDialog.ShowDirsOnly)
        if folder2Save:
            self.cbSaveFolder.insertItem(0, folder2Save)
            self.cbSaveFolder.setCurrentIndex(0)

# ---------------------------------------------------

    def show_hide_OP(self):
        if self.frMoreOp.isVisible():
            self.frMoreOp.hide()
            self.pbtnMoreOp.setText(u"More &Options")
            # self.resize(self.width(), self.height() - self.frMoreOp.height())
        else:
            self.frMoreOp.show()
            self.pbtnMoreOp.setText(u"Less &Options")
            # self.resize(self.width(), self.height() + self.frMoreOp.height())

        self.setGeometry(
            QtGui.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                                     self.size(), QtGui.QApplication.desktop().availableGeometry())
        )

# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    with open("../rc/appstyle.qss", "rt") as ssFile:
        app.setStyleSheet(ssFile.read())

    newdl_win = NewDLDLG()
    newdl_win.show()
    app.exec_()
