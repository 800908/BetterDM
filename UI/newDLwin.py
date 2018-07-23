from PyQt4 import QtGui, QtCore


# ==========START=OF=CLASS====================================


class NewDLDLG(QtGui.QDialog):

    def __init__(self, parent=None):
        super(NewDLDLG, self).__init__(parent)

        self.initUI()

# ---------------------------------------------------

    def initUI(self):
        self.setWindowTitle("BDM - New Download")
        self.setMinimumSize(450, 200)

        # ======URL========================================
        lblURL = QtGui.QLabel("File &URL:")
        self.ledtURL = QtGui.QLineEdit("")
        lblURL.setBuddy(self.ledtURL)
        lblURL.setAlignment(QtCore.Qt.AlignRight)

        # ======Size=======================================
        lblSize = QtGui.QLabel("File Size:")
        self.lblFileSize = QtGui.QLabel("")
        self.pbtnGetSize = QtGui.QPushButton("&Get Size")
        lblSize.setBuddy(self.lblFileSize)
        lblSize.setAlignment(QtCore.Qt.AlignRight)

        # ======Mirror=====================================
        lblMirror = QtGui.QLabel("&Mirror:")
        self.ledtMirror = QtGui.QLineEdit("")
        lblMirror.setBuddy(self.ledtMirror)
        lblMirror.setAlignment(QtCore.Qt.AlignRight)

        # ======File Name==================================
        lblFileName = QtGui.QLabel("&File Name:")
        self.ledtFileName = QtGui.QLineEdit("")
        lblFileName.setBuddy(self.ledtFileName)
        lblFileName.setAlignment(QtCore.Qt.AlignRight)

        # ======Folder Name================================
        lblSaveFolder = QtGui.QLabel("&Save Folder:")
        self.cbSaveFolder = QtGui.QComboBox()
        self.tbtnSaveFolder = QtGui.QToolButton()
        self.cbSaveFolder.setEditable(True)
        lblSaveFolder.setBuddy(self.cbSaveFolder)
        lblSaveFolder.setAlignment(QtCore.Qt.AlignRight)

        # ======Comment====================================
        lblComment = QtGui.QLabel("&Comment:")
        self.tedtComment = QtGui.QTextEdit("")
        lblComment.setBuddy(self.tedtComment)
        self.tedtComment.setMaximumHeight(70)
        lblComment.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)

        # ======Buttons====================================
        # hlayButtoms = QtGui.QHBoxLayout()
        self.pbtnAdd_Start = QtGui.QPushButton("&Add Start")
        self.pbtnAdd_Pause = QtGui.QPushButton("Add &Pause")
        self.pbtnCancel = QtGui.QPushButton("Cancel")
        self.pbtnMoreOp = QtGui.QPushButton("More &Option")

        # ======More Options===============================
        

        # ======Layout Manager=============================
        glayMain = QtGui.QGridLayout()

        glayMain.addWidget(lblURL, 0, 0)
        glayMain.addWidget(self.ledtURL, 0, 1, 1, 5)

        glayMain.addWidget(lblSize, 1, 0)
        glayMain.addWidget(self.pbtnGetSize, 1, 1)
        glayMain.addWidget(self.lblFileSize, 1, 2)

        glayMain.addWidget(lblMirror, 2, 0)
        glayMain.addWidget(self.ledtMirror, 2, 1, 1, 5)

        glayMain.addWidget(lblFileName, 3, 0)
        glayMain.addWidget(self.ledtFileName, 3, 1, 1, 5)

        glayMain.addWidget(lblSaveFolder, 4, 0)
        glayMain.addWidget(self.cbSaveFolder, 4, 1, 1, 4)
        glayMain.addWidget(self.tbtnSaveFolder, 4, 5)

        glayMain.addWidget(lblComment, 5, 0)
        glayMain.addWidget(self.tedtComment, 5, 1, 1, 5)

        glayMain.addWidget(self.pbtnMoreOp, 7, 0)
        glayMain.addWidget(self.pbtnCancel, 7, 3)
        glayMain.addWidget(self.pbtnAdd_Pause, 7, 4)
        glayMain.addWidget(self.pbtnAdd_Start, 7, 5)

        self.setLayout(glayMain)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    newdl_win = NewDLDLG()
    newdl_win.show()
    app.exec_()
