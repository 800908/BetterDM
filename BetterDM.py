from PyQt5 import QtWidgets, QtCore
import time
from UI.mainwin import MainWindow
from UI.newDLwin import NewDLDLG
from UI.aboutwin import AboutDLG
import UI.libs.common_func as com_func
from libs.downloader import Downloader


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
        self.Main_win.action_Download_Start.triggered.connect(
            self.on_action_Download_Start_triggered)

        self.Main_win.tblwDLs.itemSelectionChanged.connect(self.on_tblwDLs_itemSelectionChanged)

        self.RefreshDLTimer.timeout.connect(self.on_RefreshDLTimer_timout)

# ************************************************************************

    def initDefaultVals(self):
        self.DLListFileName = "downloads.json"
        self.Settings = com_func.getAppSettings()

        self.DLList = []
        self.ActiveDLList = []
        self.WaitingDLList = []

        self.RefreshDLTimer = QtCore.QTimer()
        self.RefreshDLTimer.setInterval(500)
        self.RefreshDLTimer.start()


# ************************************************************************

    def initDLList(self):
        if com_func.isFileExistInCurDir(self.DLListFileName):
            self.DLList = com_func.getFromJSONfile(self.DLListFileName)

# ************************************************************************

    def showDLList(self):
        self.Main_win.tblwDLs.setRowCount(0)  # clear table

        curRow = 0
        for curDL in self.DLList:
            self.Main_win.tblwDLs.insertRow(curRow)
            self.Main_win.tblwDLs.setItem(curRow, self.getTableColIndexByName(
                "File Name"), com_func.getNewTableItem(curDL["FileName"]))
            # self.Main_win.tblwDLs.setCellWidget(curRow, self.getTableColIndexByName(
            #     "FileSize"), com_func.getReadableFileSize(curDL["FileSize"]))
            self.Main_win.tblwDLs.setCellWidget(curRow, self.getTableColIndexByName(
                "Progress"), com_func.getNewDLProgressBar(100))
            curRow += 1

# ************************************************************************

    def saveDLList(self):
        com_func.save2JSONfile(self.DLList, self.DLListFileName)

# ************************************************************************

    def addToDLList(self, Dict2Add):
        self.DLList.append(Dict2Add)

# ************************************************************************

    def getDLDicFromNewDLWin(self, DL_win):
        DLParamDic = {}
        # DLParamDic["ID"] = com_func.getDownloadID()
        DLParamDic["ID"] = int(time.time())
        DLParamDic["Added_Time"] = time.time()
        DLParamDic["FileSize"] = 0
        DLParamDic["Downloaded"] = 0
        DLParamDic["Progress"] = 0

        DLParamDic["URL"] = str(DL_win.ledtURL.text())
        DLParamDic["Mirror"] = str(DL_win.ledtMirror.text())
        DLParamDic["FileName"] = str(DL_win.ledtFileName.text())
        DLParamDic["FilePath"] = str(DL_win.cbSaveFolder.currentText())
        DLParamDic["Comment"] = str(DL_win.tedtComment.toPlainText())
        DLParamDic["User"] = str(DL_win.ledtUser.text())
        DLParamDic["Pass"] = str(DL_win.ledtPass.text())
        DLParamDic["Proxy"] = str(DL_win.ledtProxy.text())
        DLParamDic["PxPort"] = str(DL_win.ledtPxPort.text())
        DLParamDic["MaxConn"] = DL_win.spbMaxConn.value()
        DLParamDic["ConnTimeout"] = DL_win.spbConnTimeout.value()
        DLParamDic["MaxTry"] = DL_win.spbMaxTry.value()
        DLParamDic["TryDelay"] = DL_win.spbTryDelay.value()

        # DLParamDic["Started"] = DL_win.wantedToStart

        return DLParamDic

# ************************************************************************

    def getCurDLInfoAsHtml(self, curDLDict):
        return """
                <p><strong>File Name:</strong> {0}</p>
                <p><strong>URL:</strong> <a href="{1}" target="_blank" >{1}</a></p>
                <p><strong>File Path:</strong> <a href="{2}" target="_blank" >{2}</a></p>
                <p><strong>Downloaded:</strong>{3}<strong>Remaining:</strong>{3}</p>
                <p><strong>Comment:</strong>{3}</p>
               """.format(curDLDict["FileName"], curDLDict["URL"], curDLDict["FilePath"],
                          curDLDict["Comment"])


# ************************************************************************

    def on_action_File_NewDL_triggered(self):
        NewDL_win = NewDLDLG(self.Main_win)
        NewDL_win.exec_()

        if NewDL_win.wantedToAdd:
            self.addToDLList(self.getDLDicFromNewDLWin(NewDL_win))
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

        self.Main_win.trvFiles.setRootIndex(self.Main_win.fsmFiles.setRootPath(
            self.DLList[self.Main_win.tblwDLs.currentRow()]["FilePath"]))

# ************************************************************************

    def on_action_Download_Start_triggered(self):
        self.startDownloadCurDLDict(self.DLList[self.Main_win.tblwDLs.currentRow()])

# ************************************************************************

    def on_RefreshDLTimer_timout(self):
        if len(self.ActiveDLList) > 0:
            self.updateActiveDL()

# ************************************************************************
    @QtCore.pyqtSlot(int)
    def on_Download_done(self, dlID):
        pass

# ************************************************************************

    @QtCore.pyqtSlot(int)
    def on_Download_fail(self, dlID):
        pass

# ************************************************************************

    def startDownloadCurDLDict(self, CurDict):
        DLThread = Downloader(CurDict["ID"], CurDict["URL"], CurDict["Mirror"],
                              CurDict["FileName"], CurDict["FilePath"], CurDict["FileSize"],
                              CurDict["Downloaded"], CurDict["User"], CurDict["Pass"],
                              CurDict["Proxy"], CurDict["PxPort"], CurDict["MaxConn"],
                              CurDict["ConnTimeout"])
        DLThread.doneSignal.connect(self.on_Download_done)
        DLThread.failSignal.connect(self.on_Download_fail)

        self.ActiveDLList.append({"ID": CurDict["ID"], "Downloader": DLThread})
        DLThread.start()

# ************************************************************************

    def showDLProgressOfTableRow(self, TableRow, Precent):
        pass

# ************************************************************************

    def getRowFromDLListByID(self, dlID):
        for i in range(len(self.DLList)):
            if self.DLList[i]["ID"] == dlID:
                return i

# ************************************************************************

    def getTableColIndexByName(self, ColName):
        for i in range(len(self.Main_win.TableColList)):
            if self.Main_win.TableColList[i] == ColName:
                return i

# ************************************************************************

    def updateActiveDLProgress(self):
        for ActiveDLDic in self.ActiveDLList:
            curRow = self.getDLRowFromID(ActiveDLDic["ID"])
            self.Main_win.tblwDLs.item(curRow, self.getTableColIndexByName(
                "FileSize")).setText(ActiveDLDic["Downloader"].FileSize)
            self.Main_win.tblwDLs.cellWidget(curRow, self.getTableColIndexByName(
                "Progress")).setValue(ActiveDLDic["Downloader"].Progress)
            self.Main_win.tblwDLs.item(curRow, self.getTableColIndexByName(
                "DL Speed")).setText(ActiveDLDic["Downloader"].DLSpeed)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = BetterDM(sys.argv)
    app.exec_()
