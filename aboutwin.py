from PyQt5 import QtWidgets, QtCore


# ==========START=OF=CLASS====================================

class AboutDLG(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(AboutDLG, self).__init__(parent)

        self.initUI()

# ************************************************************************

    def initUI(self):
        self.setWindowTitle("About Better Download Manager")
        # self.setGeometry(200, 100, 450, 350)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        lblLogo = QtWidgets.QLabel("Application Logo in here")
        lblLogo.setAlignment(QtCore.Qt.AlignHCenter)

        lblAppName = QtWidgets.QLabel("Better Download Manager")
        lblAppName.setAlignment(QtCore.Qt.AlignHCenter)

        lblAppVer = QtWidgets.QLabel("Ver: 0.1 alpha")
        lblAppVer.setAlignment(QtCore.Qt.AlignHCenter)

        btnClose = QtWidgets.QPushButton("&Close")
        btnClose.clicked.connect(self.close)

        grdLayout = QtWidgets.QGridLayout()
        self.setLayout(grdLayout)

        grdLayout.addWidget(lblLogo, 0, 0)
        grdLayout.addWidget(lblAppName, 1, 0)
        grdLayout.addWidget(lblAppVer, 2, 0)
        grdLayout.addWidget(btnClose, 3, 0)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_win = AboutDLG()
    about_win.show()
    app.exec_()
