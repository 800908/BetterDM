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
        self.Main_win.action_Download_Stop.triggered.connect(
            self.on_action_Download_Stop_triggered)

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
        self.RefreshDLTimer.setInterval(1000)
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
                "ID"), com_func.getNewTableItem(str(curDL["ID"])))
            self.Main_win.tblwDLs.setItem(curRow, self.getTableColIndexByName(
                "File Name"), com_func.getNewTableItem(curDL["FileName"]))
            self.Main_win.tblwDLs.setItem(curRow, self.getTableColIndexByName(
                "File Size"), com_func.getNewTableItem(com_func.getReadableFileSize(
                    curDL["FileSize"])))
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
        self.startDownloadCurTableRows()

# ************************************************************************

    def on_action_Download_Stop_triggered(self):
        self.stopDownloadCurTableRows()

# ************************************************************************

    def on_RefreshDLTimer_timout(self):
        pass
        # self.enalbe_disable_actions()

# ************************************************************************

    @QtCore.pyqtSlot(int)
    def on_Download_done(self, dl_ID):
        pass

# ************************************************************************

    @QtCore.pyqtSlot(int)
    def on_Download_fail(self, dl_ID):
        pass

# ************************************************************************

    @QtCore.pyqtSlot(int)
    def on_Download_progress(self, dl_ID):
        self.updateActiveDLProgress(dl_ID)

# ************************************************************************

    def isThisRowActiveDL(self, Row):
        if Row < 0:
            return False

        rowDL_ID = self.Main_win.tblwDLs.item(Row, self.getTableColIndexByName("ID")).text()
        for curDict in self.ActiveDLList:
            if curDict["ID"] == rowDL_ID:
                return False

        return True

# ************************************************************************

    def enalbe_disable_actions(self):
        curRow = self.Main_win.tblwDLs.currentRow()
        self.Main_win.action_Download_Start.setEnabled(
            (curRow >= 0) and self.isThisRowActiveDL(curRow))
        self.Main_win.action_Download_Stop.setEnabled(
            (curRow >= 0) and not self.Main_win.action_Download_Start.isEnabled())

# ************************************************************************

    def startDownloadCurTableRows(self):
        Rows = [SelectedRow.row()
                for SelectedRow in self.Main_win.tblwDLs.selectionModel().selectedRows()]

        for curRow in Rows:
            curRowDL_ID = int(self.Main_win.tblwDLs.item(curRow, 0).text())
            curDict = com_func.getDictByKeyValInList("ID", curRowDL_ID, self.DLList)
            isItActiveDL = com_func.isKeyValExistInDictList("ID", curRowDL_ID, self.ActiveDLList)
            if curDict and not isItActiveDL:
                DLThread = Downloader(curDict["ID"], curDict["URL"],
                                      curDict["Mirror"], curDict["FileName"],
                                      curDict["FilePath"], curDict["FileSize"],
                                      curDict["Downloaded"], curDict["User"],
                                      curDict["Pass"], curDict["Proxy"],
                                      curDict["PxPort"], curDict["MaxConn"],
                                      curDict["ConnTimeout"])
                DLThread.doneSignal.connect(self.on_Download_done)
                DLThread.failSignal.connect(self.on_Download_fail)
                DLThread.progressSignal.connect(self.on_Download_progress)

                self.ActiveDLList.append({"ID": curDict["ID"], "Downloader": DLThread})
                DLThread.start()

# ************************************************************************

    def stopDownloadCurTableRows(self):
        Rows = [SelectedRow.row()
                for SelectedRow in self.Main_win.tblwDLs.selectionModel().selectedRows()]

        for curRow in Rows:
            curRowDL_ID = int(self.Main_win.tblwDLs.item(curRow, 0).text())
            isItActiveDL = com_func.isKeyValExistInDictList("ID", curRowDL_ID, self.ActiveDLList)
            if isItActiveDL:
                curDict = com_func.getDictByKeyValInList("ID", curRowDL_ID, self.ActiveDLList)
                DLThread = curDict["Downloader"]
                if DLThread.isRunning():
                    DLThread.terminate()
                    self.ActiveDLList.remove(curDict)

# ************************************************************************

    def showDLProgressOfTableRow(self, TableRow, Precent):
        pass

# ************************************************************************

    def getTableColIndexByName(self, ColName):
        for i in range(len(self.Main_win.TableColList)):
            if self.Main_win.TableColList[i] == ColName:
                return i

# ************************************************************************
    def getRowIndexOfDLByID

    def updateActiveDLProgress(self, dl_ID):
        dl_Dict = com_func.getDictByKeyValInList("ID", dl_ID, ActiveDLList)

        # for ActiveDLDic in self.ActiveDLList:
        #     curRow = self.getDLRowFromID(ActiveDLDic["ID"])
        #     self.Main_win.tblwDLs.item(curRow, self.getTableColIndexByName(
        #         "FileSize")).setText(ActiveDLDic["Downloader"].FileSize)
        #     self.Main_win.tblwDLs.cellWidget(curRow, self.getTableColIndexByName(
        #         "Progress")).setValue(ActiveDLDic["Downloader"].Progress)
        #     self.Main_win.tblwDLs.item(curRow, self.getTableColIndexByName(
        #         "DL Speed")).setText(ActiveDLDic["Downloader"].DLSpeed)


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = BetterDM(sys.argv)
    app.exec_()
