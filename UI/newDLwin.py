from PyQt4 import QtGui, QtCore


# ==========START=OF=CLASS====================================


class NewDLDLG(QtGui.QDialog):

    def __init__(self, parent=None):
        super(NewDLDLG, self).__init__(parent)

        self.initUI()

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

        # ======Buttons====================================
        # hlayButtoms = QtGui.QHBoxLayout()
        self.pbtnAdd_Start = QtGui.QPushButton(u"&Add Start")
        self.pbtnAdd_Pause = QtGui.QPushButton(u"Add &Pause")
        self.pbtnCancel = QtGui.QPushButton(u"Cancel")
        self.pbtnMoreOp = QtGui.QPushButton(u"More &Options")

        # ======More Options===============================
        self.gboxMoreOp = QtGui.QGroupBox()
        # self.gboxMoreOp.setContentsMargins(5, 5, 5, 5)

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

        # glayMoreOp = QtGui.QGridLayout()

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

        # glayMain.addWidget(gboxConn, 6, 0, 1, 3)
        # glayMain.addWidget(gboxID, 6, 3, 1, 4)

        # glayMain.addWidget(self.pbtnMoreOp, 7, 0, 1, 2)
        # glayMain.addWidget(self.pbtnCancel, 7, 7)
        # glayMain.addWidget(self.pbtnAdd_Pause, 7, 8)
        # glayMain.addWidget(self.pbtnAdd_Start, 7, 9)

        self.setLayout(glayMain)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    with open("../rc/appstyle.qss", "rt") as ssFile:
        app.setStyleSheet(ssFile.read())

    newdl_win = NewDLDLG()
    newdl_win.show()
    app.exec_()
