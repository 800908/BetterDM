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

        # ======Layout=====================================
        glayMain = QtGui.QGridLayout()
        glayMain.setColumnStretch(1, 5)

        glayMain.addWidget(lblURL, 0, 0)
        glayMain.addWidget(self.ledtURL, 0, 1, 1, 2)

        glayMain.addWidget(lblMirror, 1, 0)
        glayMain.addWidget(self.ledtMirror, 1, 1, 1, 2)

        glayMain.addWidget(lblFileName, 2, 0)
        glayMain.addWidget(self.ledtFileName, 2, 1, 1, 2)

        glayMain.addWidget(lblSaveFolder, 3, 0)
        glayMain.addWidget(self.cbSaveFolder, 3, 1)
        glayMain.addWidget(self.tbtnSaveFolder, 3, 2)

        glayMain.addWidget(lblComment, 4, 0)
        glayMain.addWidget(self.tedtComment, 4, 1, 2, 2)

        self.setLayout(glayMain)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    newdl_win = NewDLDLG()
    newdl_win.show()
    app.exec_()
