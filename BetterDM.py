from PyQt5 import QtWidgets
from UI.mainwin import MainWindow
from UI.newDLwin import NewDLDLG
from UI.aboutwin import AboutDLG
import UI.libs.common_func as com_func


# ==========START=OF=CLASS====================================

class BetterDM(QtWidgets.QApplication):

    def __init__(self, argv):
        super(BetterDM, self).__init__(argv)

        self.Main_win = MainWindow()
        self.initMainWin()
        self.initDefaultVals()
        self.initDLList()
        self.Main_win.show()


# ---------------------------------------------------

    def initMainWin(self):
        self.initMainWinActions()

# ---------------------------------------------------

    def initMainWinActions(self):
        self.Main_win.action_File_NewDL.triggered.connect(self.on_action_File_NewDL_triggered)
        self.Main_win.action_Help_About.triggered.connect(self.on_action_Help_About_triggered)

# ---------------------------------------------------

    def initDefaultVals(self):
        self.DLListFileName = "downloads.json"

# ---------------------------------------------------

    def initDLList(self):
        self.DLList = []


# ---------------------------------------------------

    def loadDLList():
        pass

# ---------------------------------------------------

    def showDLListInTable(self):
        curRow = 0
        for curDL in self.DLList:
            self.Main_win.tblwDLs.insertRow(curRow)
            self.Main_win.tblwDLs.setItem(curRow, 0, com_func.getNewTableItem(
                curDL["FileName"]))
            self.Main_win.tblwDLs.setItem(curRow, 1, com_func.getNewTableItem(
                curDL["Mirror"]))
            self.Main_win.tblwDLs.setItem(curRow, 2, com_func.getNewTableItem(
                curDL["FileName"]))
            curRow += 1

# ---------------------------------------------------

    def addToDLList(self, toADDdic):
        self.DLList.append(toADDdic)
        self.showDLListInTable()


# ---------------------------------------------------

    def getDLDicfromNewDLWin(self, DL_win):
        DLParamDic = {}
        DLParamDic["URL"] = str(DL_win.ledtURL.text())
        DLParamDic["Mirror"] = str(DL_win.ledtMirror.text())
        DLParamDic["FileName"] = str(DL_win.ledtFileName.text())
        DLParamDic["FileFolder"] = str(DL_win.cbSaveFolder.currentText())
        DLParamDic["Comment"] = str(DL_win.tedtComment.toPlainText())
        DLParamDic["Started"] = DL_win.wantedToStart

        return DLParamDic

# ---------------------------------------------------

    def on_action_File_NewDL_triggered(self):
        NewDL_win = NewDLDLG(self.Main_win)
        NewDL_win.exec_()

        if NewDL_win.wantedToAdd:
            self.addToDLList(self.getDLDicfromNewDLWin(NewDL_win))

# ---------------------------------------------------

    def on_action_Help_About_triggered(self):
        AboutMe_win = AboutDLG(self.Main_win)
        AboutMe_win.exec_()


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = BetterDM(sys.argv)
    app.exec_()
