import json
import time
import os

# ==========START=OF=CLASS====================================


class DLDataManager():

    def __init__(self):
        self.defineVariables()

# ************************************************************************

    def defineVariables(self):
        self.ID_str = "ID"
        self.AddedTime_str = "Added_Time"
        self.FileSize_str = "FileSize"
        self.Downloaded_str = "Downloaded"
        self.Progress_str = "Progress"
        self.URL_str = "URL"
        self.Mirror_str = "Mirror"
        self.FileName_str = "FileName"
        self.FilePath_str = "FilePath"
        self.Comment_str = "Comment"
        self.User_str = "User"
        self.Pass_str = "Pass"
        self.Proxy_str = "Proxy"
        self.PxPort_str = "PxPort"
        self.MaxConn_str = "MaxConn"
        self.ConnTimeout_str = "ConnTimeout"
        self.MaxTry_str = "MaxTry"
        self.TryDelay_str = "TryDelay"

        self.JsonFileName = "downloads.json"
        self.AllDLList = []
        self.ActiveDLList = []
        self.WatingDLList = []

# ************************************************************************

    def getDLDataFromNewDLWinAsDict(self, DL_win):
        Result = {}

        Result[self.ID_str] = int(time.time())
        Result[self.AddedTime_str] = time.time()
        Result[self.FileSize_str] = 0
        Result[self.Downloaded_str] = 0
        Result[self.Progress_str] = 0

        Result[self.URL_str] = str(DL_win.ledtURL.text())
        Result[self.Mirror_str] = str(DL_win.ledtMirror.text())
        Result[self.FileName_str] = str(DL_win.ledtFileName.text())
        Result[self.FilePath_str] = str(DL_win.cbSaveFolder.currentText())
        Result[self.Comment_str] = str(DL_win.tedtComment.toPlainText())
        Result[self.User_str] = str(DL_win.ledtUser.text())
        Result[self.Pass_str] = str(DL_win.ledtPass.text())
        Result[self.Proxy_str] = str(DL_win.ledtProxy.text())
        Result[self.PxPort_str] = str(DL_win.ledtPxPort.text())
        Result[self.MaxConn_str] = DL_win.spbMaxConn.value()
        Result[self.ConnTimeout_str] = DL_win.spbConnTimeout.value()
        Result[self.MaxTry_str] = DL_win.spbMaxTry.value()
        Result[self.TryDelay_str] = DL_win.spbTryDelay.value()

        return Result

# ************************************************************************

    def saveData2JSONfile(toSave, jsonFileName):
        try:
            with open(jsonFileName, "wt") as outFile:
                json.dump(toSave, outFile)
        except IOError:
            return -1

# ************************************************************************

    def getDataFromJSONfile(jsonFileName):
        try:
            with open(jsonFileName, "rt") as inFile:
                return json.load(inFile)
        except IOError:
            return -1

# ************************************************************************

    def initDLList(self):
        if os.path.exists(self.JsonFileName):
            self.AllDLList = self.getDataFromJSONfile(self.JsonFileName)

# ************************************************************************

    def saveDLList(self):
        self.saveData2JSONfile(self.AllDLList, self.JsonFileName)

# ************************************************************************
