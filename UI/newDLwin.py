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

        lblURL = QtGui.QLabel("File &URL:")
        self.ledtURL = QtGui.QLineEdit("")
        lblURL.setBuddy(self.ledtURL)
        lblURL.setAlignment(QtCore.Qt.AlignRight)

        lblMirror = QtGui.QLabel("&Mirror:")
        self.ledtMirror = QtGui.QLineEdit("")
        lblMirror.setBuddy(self.ledtMirror)
        lblMirror.setAlignment(QtCore.Qt.AlignRight)

        lblFileName = QtGui.QLabel("&File Name:")
        self.ledtFileName = QtGui.QLineEdit("")
        lblFileName.setBuddy(self.ledtFileName)
        lblFileName.setAlignment(QtCore.Qt.AlignRight)

        glayMain = QtGui.QGridLayout()

        glayMain.addWidget(lblURL, 0, 0)
        glayMain.addWidget(self.ledtURL, 0, 1)
        glayMain.addWidget(lblMirror, 1, 0)
        glayMain.addWidget(self.ledtMirror, 1, 1)
        glayMain.addWidget(lblFileName, 2, 0)
        glayMain.addWidget(self.ledtFileName, 2, 1)

        self.setLayout(glayMain)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    newdl_win = NewDLDLG()
    newdl_win.show()
    app.exec_()
