import pycurl
import os
import time
import datetime
import math
from PyQt5.QtCore import QThread, pyqtSignal


# ==========START=OF=CLASS====================================

class CURLDownloader():

    def __init__(self, dlID, dlURL, dlMirror, dlFileName, dlFilePath, dlFileSize, dlDownloaded,
                 dlUser, dlPass, dlProxy, dlPxPort, dlMaxConn, dlConnTimeout):

        self.ID = int(dlID)
        self.FileURL = dlURL
        self.FileMirror = dlMirror
        self.FileName = dlFileName
        self.FilePath = dlFilePath

        if dlFileSize == 0:
            self.FileSize = self.getFileSize(dlURL)
        else:
            self.FileSize = dlFileSize

        self.UserPass = dlUser + ":" + dlPass
        self.Proxy = dlProxy
        self.PxPort = dlPxPort
        self.MaxConn = dlMaxConn
        self.ConnTimeout = dlConnTimeout

        self.ToDownload = self.FileSize
        self.Downloaded = dlDownloaded

        self.doneSignal = pyqtSignal(int)
        self.failSignal = pyqtSignal(int)
        self.progressSignal = pyqtSignal(int)

        self.FailReason = ""
        self.StartTime = time.time()
        self.LastTime = self.StartTime
        self.LastTimeDL = 0

        self.initCurl()


# ************************************************************************

    def startDownload(self):
        try:
            self.CURL.perform()
            self.doneSignal.emit(self.ID)
        except pycurl.error as error:
            self.FailReason = str(error)
            self.failSignal.emit(self.ID)
        finally:
            self.CURL.close()
            self.writefunc.close()

# ************************************************************************

    def initCurl(self):
        self.CURL = pycurl.Curl()

        self.CURL.setopt(pycurl.VERBOSE, 0)
        self.CURL.setopt(pycurl.NOPROGRESS, 0)
        self.CURL.setopt(pycurl.FOLLOWLOCATION, 1)
        self.CURL.setopt(pycurl.MAXREDIRS, 5)

        self.CURL.setopt(pycurl.URL, self.FileURL)
        self.CURL.setopt(pycurl.MAXFILESIZE_LARGE, self.FileSize)
        self.CURL.setopt(pycurl.USERPWD, self.UserPass)
        self.CURL.setopt(pycurl.PROXY, self.Proxy)
        self.CURL.setopt(pycurl.PROXYPORT, self.PxPort)
        self.CURL.setopt(pycurl.MAXCONNECTS, self.MaxConn)
        self.CURL.setopt(pycurl.CONNECTTIMEOUT, self.ConnTimeout)

        if os.path.exists(self.FilePath + self.FileName):
            self.writefunc = open(self.FilePath + self.FileName, "ab")
            self.CURL.setopt(pycurl.RESUME_FROM, os.path.getsize(self.FilePath + self.FileName))
        else:
            self.writefunc = open(self.FilePath + self.FileName, "wb")

        self.CURL.setopt(pycurl.WRITEDATA, self.writefunc)
        self.CURL.setopt(pycurl.PROGRESSFUNCTION, self.progressInfo)

# ************************************************************************

    def progressInfo(self, Total2DL, TotalDLed, Total2UL, TotalULed):

        self.Progress = (os.path.getsize(self.FilePath + self.FileName) / self.FileSize) * 100

        curDLed = TotalDLed - self.LastTimeTotalDL
        curTime = time.time()
        diffTime = curTime - self.LastTime
        self.DLSpeed = self.getReadableFileSize(int(curDLed / diffTime)) + "/s"
        self.LastTimeTotalDL = TotalDLed
        self.LastTime = curTime

        self.RemainingByte = Total2DL - TotalDLed
        averageSpeed = TotalDLed / (curTime - self.StartTime)
        self.RemainigTime = str(datetime.timedelta(seconds=self.RemainingByte / averageSpeed))

        self.progressSignal.emit(self.ID)


# ************************************************************************

    def getFileSize(self, FileURL):
        try:
            CURL = pycurl.Curl()
            CURL.setopt(CURL.URL, FileURL)
            CURL.setopt(CURL.NOBODY, 1)
            CURL.perform()
            return CURL.getinfo(CURL.CONTENT_LENGTH_DOWNLOAD)
        except pycurl.error:
            return 0

# ************************************************************************
# from: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    def getReadableFileSize(self, SizeInBytes):
        if SizeInBytes <= 0:
            return "0B"

        SizeName = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(SizeInBytes, 1024)))
        p = math.pow(1024, i)
        s = round(SizeInBytes / p, 2)

        return "{} {}".format(s, SizeName[i])


# ==========START=OF=CLASS====================================

class Downloader(CURLDownloader, QThread):

    def __init__(self, dlID, dlURL, dlMirror, dlFileName, dlFilePath, dlFileSize, dlDownloaded,
                 dlUser, dlPass, dlProxy, dlPxPort, dlMaxConn, dlConnTimeout):

        QThread.__init__(self)
        CURLDownloader.__init__(self, dlID, dlURL, dlMirror, dlFileName, dlFilePath, dlFileSize,
                                dlDownloaded, dlUser, dlPass, dlProxy, dlPxPort, dlMaxConn,
                                dlConnTimeout)

# ************************************************************************

    def __del__(self):
        self.wait()

# ************************************************************************

    def run(self):
        self.startDownload()

# =================================================================
