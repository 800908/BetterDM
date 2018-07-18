from PyQt4 import QtGui


# ==========START=OF=CLASS====================================

class AboutDLG(QtGui.QDialog):

    def __init__(self, parent=None):
        super(AboutDLG, self).__init__(parent)

        self.initUI()

    def initUI(self):
        pass

# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    about_win = AboutDLG()
    about_win.show()

    app.exec_()
