from PyQt5 import QtWidgets
import time
from UI.mainwin import MainWindow
from UI.newDLwin import NewDLDLG
from UI.aboutwin import AboutDLG
import UI.libs.common_func as com_func


# ==========START=OF=CLASS====================================

class BetterDM(QtWidgets.QApplication):

    def __init__(self, argv):
        super(BetterDM, self).__init__(argv)

        self.initDefaultVals()
        self.initDLList()

        self.Main_win = MainWindow()
        self.initMainWin()

        self.initEventHandler()
        self.load_apply_AppSettings()

        self.Main_win.show()

# ************************************************************************

    def initMainWin(self):
        self.showDLList()

# ************************************************************************

    def load_apply_AppSettings(self):
        pass


# ************************************************************************

    def initEventHandler(self):
        self.Main_win.action_File_NewDL.triggered.connect(self.on_action_File_NewDL_triggered)
        self.Main_win.action_Help_About.triggered.connect(self.on_action_Help_About_triggered)

        self.Main_win.tblwDLs.itemSelectionChanged.connect(self.on_tblwDLs_itemSelectionChanged)

# ************************************************************************

    def initDefaultVals(self):
        self.DLListFileName = "downloads.json"
        self.Settings = com_func.getAppSettings()

# ************************************************************************

    def initDLList(self):
        if com_func.isFileExistInCurDir(self.DLListFileName):
            self.DLList = com_func.getFromJSONfile(self.DLListFileName)
        else:
            self.DLList = []

# ************************************************************************

    def showDLList(self):
        self.Main_win.tblwDLs.setRowCount(0)  # clear table

        curRow = 0
        for curDL in self.DLList:
            self.Main_win.tblwDLs.insertRow(curRow)
            self.Main_win.tblwDLs.setItem(curRow, 0, com_func.getNewTableItem(
                curDL["FileName"]))
            # self.Main_win.tblwDLs.setItem(curRow, 1, com_func.getNewTableItem(
            #     curDL["Size"]))

            self.Main_win.tblwDLs.setCellWidget(curRow, 2, com_func.getNewDLProgressBar(100))
            curRow += 1

# ************************************************************************

    def saveDLList(self):
        com_func.save2JSONfile(self.DLList, self.DLListFileName)

# ************************************************************************

    def addToDLList(self, Dict2Add):
        self.DLList.append(Dict2Add)

# ************************************************************************

    def getDLDicfromNewDLWin(self, DL_win):
        DLParamDic = {}
        DLParamDic["URL"] = str(DL_win.ledtURL.text())
        DLParamDic["Mirror"] = str(DL_win.ledtMirror.text())
        DLParamDic["FileName"] = str(DL_win.ledtFileName.text())
        DLParamDic["FileFolder"] = str(DL_win.cbSaveFolder.currentText())
        DLParamDic["Comment"] = str(DL_win.tedtComment.toPlainText())
        DLParamDic["Started"] = DL_win.wantedToStart
        DLParamDic["Added_Time"] = time.time()

        return DLParamDic

# ************************************************************************

    def getCurDLInfoAsHtml(self, curDLDict):
        return """
                <p><strong>File Name:</strong> {0}</p>
                <p><strong>URL:</strong> <a href="{1}" target="_blank" >{1}</a></p>
                <p><strong>File Path:</strong> <a href="{2}" target="_blank" >{2}</a></p>
                <p><strong>Comment:</strong>{3}</p>
               """.format(curDLDict["FileName"], curDLDict["URL"], curDLDict["FileFolder"],
                          curDLDict["Comment"])


# ************************************************************************

    def on_action_File_NewDL_triggered(self):
        NewDL_win = NewDLDLG(self.Main_win)
        NewDL_win.cbSaveFolder.addItems(com_func.getValFromAppSettings(
            "NewDL_win/cbSaveFolderItems", [com_func.getSysDLDir()]))
        NewDL_win.exec_()

        if NewDL_win.wantedToAdd:
            self.addToDLList(self.getDLDicfromNewDLWin(NewDL_win))
            self.saveDLList()
            self.showDLList()


# ************************************************************************

    def on_action_Help_About_triggered(self):
        AboutMe_win = AboutDLG(self.Main_win)
        AboutMe_win.exec_()

# ************************************************************************

    def on_tblwDLs_itemSelectionChanged(self):
        self.Main_win.tedtDLInfo.setHtml(self.getCurDLInfoAsHtml(
            self.DLList[self.Main_win.tblwDLs.currentRow()]))


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = BetterDM(sys.argv)
    app.exec_()
