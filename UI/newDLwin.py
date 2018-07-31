from PyQt5 import QtWidgets, QtCore
import res.ui_common_func as com_func

# ==========START=OF=CLASS====================================


class NewDLDLG(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(NewDLDLG, self).__init__(parent)

        self.initUI()
        self.initEventHandlers()

# ---------------------------------------------------

    def initUI(self):
        self.setWindowTitle(u"BDM - New Download")
        self.setMinimumSize(450, 200)

        # ======URL========================================
        self.ledtURL = QtWidgets.QLineEdit("")
        lblURL = com_func.getBuddyLabel(u"File &URL:", self.ledtURL)

        # ======Size=======================================
        self.pbtnGetSize = QtWidgets.QPushButton(u"&Get Size")
        lblSize = com_func.getBuddyLabel(u"File Size:", self.pbtnGetSize)
        self.lblFileSize = QtWidgets.QLabel("")

        # ======Mirror=====================================
        self.ledtMirror = QtWidgets.QLineEdit("")
        lblMirror = com_func.getBuddyLabel(u"&Mirror:", self.ledtMirror)

        # ======File Name==================================
        self.ledtFileName = QtWidgets.QLineEdit("")
        lblFileName = com_func.getBuddyLabel(u"&File Name:", self.ledtFileName)

        # ======Folder Name================================
        self.cbSaveFolder = QtWidgets.QComboBox()
        self.tbtnSaveFolder = QtWidgets.QToolButton()
        self.cbSaveFolder.setEditable(True)
        lblSaveFolder = com_func.getBuddyLabel(u"&Save Folder:", self.cbSaveFolder)

        # ======Comment====================================
        self.tedtComment = QtWidgets.QTextEdit("")
        lblComment = com_func.getBuddyLabel(u"&Comment:", self.tedtComment)
        self.tedtComment.setMaximumHeight(70)
        lblComment.setAlignment(QtCore.Qt.AlignTop)

        # ======More Options===============================

        # ------Connections Group--------------------------
        self.spbMaxConn = QtWidgets.QSpinBox()
        self.spbMaxConn.setValue(4)
        self.spbMaxConn.setMinimum(1)
        self.spbMaxConn.setMaximum(16)
        lblMaxConn = com_func.getBuddyLabel(u"Ma&x Connections:", self.spbMaxConn)

        self.spbMaxTry = QtWidgets.QSpinBox()
        self.spbMaxTry.setValue(10)
        self.spbMaxTry.setMinimum(1)
        self.spbMaxTry.setMaximum(999)
        lblMaxTry = com_func.getBuddyLabel(u"Max &Try:", self.spbMaxTry)

        self.spbTryDelay = QtWidgets.QSpinBox()
        self.spbTryDelay.setValue(5)
        self.spbTryDelay.setMinimum(1)
        self.spbTryDelay.setMaximum(99)
        lblTryDelay = com_func.getBuddyLabel(u"Trying &Delay:", self.spbTryDelay)

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
        lblUserName = com_func.getBuddyLabel(u"&User Name:", self.ledtUser)

        self.ledtPass = QtWidgets.QLineEdit("")
        lblPassword = com_func.getBuddyLabel(u"&Password:", self.ledtPass)

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
        self.frMoreOp.setLayout(glayMoreOp)
        self.frMoreOp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frMoreOp.hide()

        # ======Bottom Line================================
        frBottomLine = QtWidgets.QFrame()
        frBottomLine.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Sunken)

        # ======Buttons====================================
        self.pbtnAdd_Start = QtWidgets.QPushButton(u"&Add Start")
        self.pbtnAdd_Pause = QtWidgets.QPushButton(u"Add &Pause")
        self.pbtnCancel = QtWidgets.QPushButton(u"Cancel")
        self.pbtnMoreOp = QtWidgets.QPushButton(u"More &Options")
        # self.pbtnMoreOp.setCheckable(True)

        hlayButtons = QtWidgets.QHBoxLayout()
        hlayButtons.addWidget(self.pbtnMoreOp)
        hlayButtons.insertSpacing(1, 50)
        hlayButtons.addWidget(self.pbtnCancel)
        hlayButtons.addWidget(self.pbtnAdd_Pause)
        hlayButtons.addWidget(self.pbtnAdd_Start)

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

        glayMain.addWidget(self.frMoreOp, 6, 0, 1, 10)

        glayMain.addWidget(frBottomLine, 7, 0, 1, 10)

        glayMain.addLayout(hlayButtons, 8, 0, 1, 10)

        glayMain.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.setLayout(glayMain)

# ---------------------------------------------------

    def initEventHandlers(self):
        self.pbtnMoreOp.clicked.connect(self.show_hide_OP)
        self.tbtnSaveFolder.clicked.connect(self.setFolder2Save)

# ---------------------------------------------------
    def setFolder2Save(self):
        fdSaveFolder = QtWidgets.QFileDialog()

        folder2Save = fdSaveFolder.getExistingDirectory(
            self, u"Please choose a folder to save on",
            com_func.getSysDLDir(),
            QtWidgets.QFileDialog.ShowDirsOnly)

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
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, self.size(),
                QtWidgets.QApplication.desktop().availableGeometry())
        )

# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    with open("../rc/appstyle.qss", "rt") as ssFile:
        app.setStyleSheet(ssFile.read())

    newdl_win = NewDLDLG()
    newdl_win.show()
    app.exec_()
