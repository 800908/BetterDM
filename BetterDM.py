from PyQt5 import QtWidgets, QtCore
import time
from mainwin import MainWindow
from newDLwin import NewDLDLG
from aboutwin import AboutDLG
import libs.common_func as com_func
from downloader import Downloader
from dldatamanager import DLDataMan


# ==========START=OF=CLASS====================================

class BetterDM(QtWidgets.QApplication):

    def __init__(self, argv):
        super(BetterDM, self).__init__(argv)

        self.initDefaultVals()
        # self.initDLList()

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
        self.DLDataMan = DLDataMan()
        self.Settings = com_func.getAppSettings()

        self.RefreshDLTimer = QtCore.QTimer()
        self.RefreshDLTimer.setInterval(1000)
        self.RefreshDLTimer.start()

# ************************************************************************

    def showDLList(self):
        Table = self.Main_win.tblwDLs
        Table.showDataInTable(self.DLDataMan.AllDLList)

# ************************************************************************

    def addToDLList(self, Dict2Add):
        self.DLList.append(Dict2Add)

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
        Table = self.Main_win.tblwDLs
        self.Main_win.tedtDLInfo.setHtml(self.getCurDLInfoAsHtml(
            self.DLList[Table.currentRow()]))

        self.Main_win.trvFiles.setRootIndex(self.Main_win.fsmFiles.setRootPath(
            self.DLList[Table.currentRow()]["FilePath"]))

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
        Table = self.Main_win.tblwDLs
        Rows = [SelectedRow.row() for SelectedRow in Table.selectionModel().selectedRows()]

        for curRow in Rows:
            curRowDL_ID = int(Table.item(curRow, 0).text())
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
        Table = self.Main_win.tblwDLs
        Rows = [SelectedRow.row() for SelectedRow in Table.selectionModel().selectedRows()]

        for curRow in Rows:
            curRowDL_ID = int(Table.item(curRow, 0).text())
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

    def getRowIndexByID(self, RowID):
        Table = self.Main_win.tblwDLs
        for curRowIndex in range(Table.rowCount()):
            if int(Table.item(curRowIndex, 0).text()) == RowID:
                return curRowIndex

        return -1

# ************************************************************************
    def updateActiveDLProgress(self, dl_ID):
        Table = self.Main_win.tblwDLs
        RowIndex = self.getRowIndexByID(dl_ID)

        if RowIndex == -1:  # if not visible
            return

        dl_Dict = com_func.getDictByKeyValInList("ID", dl_ID, self.ActiveDLList)
        dl_Thread = dl_Dict["Downloader"]

        FileSizeItem = Table.item(RowIndex, self.getTableColIndexByName("File Size"))
        DLSpeedItem = Table.item(RowIndex, self.getTableColIndexByName("DL Speed"))
        TimeToFinishItem = Table.item(RowIndex, self.getTableColIndexByName("Time to Finish"))
        ProgressItem = Table.cellWidget(RowIndex, self.getTableColIndexByName("Progress"))

        FileSizeItem.setText(com_func.getReadableFileSize(dl_Thread.FileSize))
        DLSpeedItem.setText(dl_Thread.DLSpeed)
        TimeToFinishItem.setText(dl_Thread.RemainingTime)
        ProgressItem.setValue(int(dl_Thread.Progress))


# ============END=OF=CLASS====================================


if __name__ == "__main__":
    import sys
    app = BetterDM(sys.argv)
    app.exec_()
