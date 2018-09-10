import pycurl
import os


# ==========START=OF=CLASS====================================

class Downloader():

    def __init__(self, FileInfoDict, Table2Show, RowInTable):

        self.initVariables(FileInfoDict)

        self.initCurl(FileInfoDict)


# ************************************************************************

    def initVariables(self, FileInfoDict):
        if FileInfoDict["FileSize"] == "":
            self.FileSize = self.getFileSize(FileInfoDict["URL"])
        else:
            self.FileSize = FileInfoDict["FileSize"]

        self.FileURL = FileInfoDict["URL"]
        self.FileMirror = FileInfoDict["Mirror"]
        self.FilePath = FileInfoDict["FilePath"]

# ************************************************************************

    def initCurl(self, FileInfoDict):
        self.CURL = pycurl.Curl()

        self.CURL.setopt(pycurl.VERBOSE, 0)
        self.CURL.setopt(pycurl.NOPROGRESS, 0)
        self.CURL.setopt(pycurl.FOLLOWLOCATION, 1)
        self.CURL.setopt(pycurl.MAXREDIRS, 3)

        self.CURL.setopt(pycurl.URL, FileInfoDict["URL"])
        self.CURL.setopt(pycurl.MAXFILESIZE_LARGE, FileInfoDict["FileSize"])
        self.CURL.setopt(pycurl.USERPWD, FileInfoDict["URL"])
        self.CURL.setopt(pycurl.PROXY, FileInfoDict["URL"])
        self.CURL.setopt(pycurl.PROXYPORT, FileInfoDict["URL"])

        if os.path.exists(self.FilePath + self.FileName):
            writefunc = open(self.FilePath + self.FileName, "ab")
            self.CURL.setopt(pycurl.RESUME_FROM, os.path.getsize(self.FilePath + self.FileName))
        else:
            writefunc = open(self.FilePath + self.FileName, "wb")

        self.CURL.setopt(pycurl.WRITEDATA, writefunc)
        # self.CURL.setopt(pycurl.PROGRESSFUNCTION, progress)

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
