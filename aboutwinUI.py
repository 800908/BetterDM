from PyQt4 import QtGui, QtCore


# ==========START=OF=CLASS====================================

class AboutDLG(QtGui.QDialog):

    def __init__(self, parent=None):
        super(AboutDLG, self).__init__(parent)

        self.initUI()

# ---------------------------------------------------

    def initUI(self):
        self.setWindowTitle("About Better Download Manager")
        self.setGeometry(200, 100, 450, 350)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint)

        lblLogo = QtGui.QLabel("Application Logo in here")
        lblLogo.setAlignment(QtCore.Qt.AlignHCenter)

        lblAppName = QtGui.QLabel("Better Download Manager")
        lblAppName.setAlignment(QtCore.Qt.AlignHCenter)

        lblAppVer = QtGui.QLabel("Ver: 0.1 alpha")
        lblAppVer.setAlignment(QtCore.Qt.AlignHCenter)

        btnClose = QtGui.QPushButton("&Close")
        btnClose.clicked.connect(self.close)

        grdLayout = QtGui.QGridLayout()
        self.setLayout(grdLayout)

        grdLayout.addWidget(lblLogo, 0, 0)
        grdLayout.addWidget(lblAppName, 1, 0)
        grdLayout.addWidget(lblAppVer, 2, 0)
        grdLayout.addWidget(btnClose, 3, 0)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    about_win = AboutDLG()
    about_win.show()
    app.exec_()
