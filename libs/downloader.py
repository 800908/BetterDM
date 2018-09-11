import pycurl
import os


# ==========START=OF=CLASS====================================

class CURLDownloader():

    def __init__(self, dlURL, dlMirror, dlFileName, dlFilePath, dlFileSize,
                 dlUser, dlPass, dlProxy, dlPxPort, dlMaxConn, dlConnTimeout):

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
        self.Failed = False
        self.FailReason = ""

        self.initCurl()

        try:
            self.CURL.perform()
        except pycurl.error as error:
            self.Failed = True
            self.FailReason = str(error)
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

    def progressInfo(self, Total2DL, Downloaded, Total2UL, Uploaded):
        self.ToDownload = Total2DL
        self.Downloaded = Downloaded

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
