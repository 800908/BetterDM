from PyQt4 import QtGui, QtCore


# ==========START=OF=CLASS====================================

class AboutDLG(QtGui.QDialog):

    def __init__(self, parent=None):
        super(AboutDLG, self).__init__(parent)

        self.initUI()

# ---------------------------------------------------

    def initUI(self):
        self.setWindowTitle("About Better Download Manager")
        self.resize(450, 350)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint)

# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    about_win = AboutDLG()
    about_win.show()
    app.exec_()
