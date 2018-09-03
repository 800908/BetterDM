from PyQt5 import QtWidgets
from UI.mainwin import MainWindow
from UI.newDLwin import NewDLDLG
from UI.aboutwin import AboutDLG
# import UI.res.ui_common_func as com_func


# ==========START=OF=CLASS====================================

class BetterDM(QtWidgets.QApplication):

    def __init__(self, argv):
        super(BetterDM, self).__init__(argv)

        self.Main_win = MainWindow()
        self.initMainWin()
        self.Main_win.show()

# ---------------------------------------------------

    def initMainWin(self):
        self.initMainWinActions()

# ---------------------------------------------------

    def initMainWinActions(self):
        self.Main_win.action_File_NewDL.triggered.connect(self.NewDownload)
        self.Main_win.action_Help_About.triggered.connect(self.show_AboutMe)


# ---------------------------------------------------

    def NewDownload(self):
        NewDL_win = NewDLDLG(self.Main_win)
        NewDL_win.exec_()

        if NewDL_win.wantedToAdd:
            pass


# ---------------------------------------------------

    def show_AboutMe(self):
        AboutMe_win = AboutDLG(self.Main_win)
        AboutMe_win.exec_()


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = BetterDM(sys.argv)
    app.exec_()
