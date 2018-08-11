from PyQt5 import QtWidgets, QtCore, QtGui
import pycurl
import math
import re
import json

# ---------------------------------------------------------------------------


def getNewAction(parent=None, actTitle="New Action", actShortcut="", actTip="", actTriger=None):
    Result = QtWidgets.QAction(actTitle, parent)
    Result.setShortcut(actShortcut)
    Result.setToolTip(actTip)
    Result.setStatusTip(actTip)
    if actTriger:
        Result.triggered.connect(actTriger)

    return Result

# ---------------------------------------------------------------------------


def getNewBuddyLabel(title, buddy, parent=None):
    Result = QtWidgets.QLabel(title, parent)
    Result.setBuddy(buddy)

    return Result

# ---------------------------------------------------------------------------


def getNewTableItem(itemToGet):
    Result = QtWidgets.QTableWidgetItem(itemToGet)
    Result.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

    return Result


# ---------------------------------------------------------------------------

def showErrorMessBox(title, message, parent=None):
    MessBox = QtWidgets.QMessageBox(parent)
    MessBox.setIcon(QtWidgets.QMessageBox.Critical)
    MessBox.setWindowTitle(title)
    MessBox.setText(message)
    MessBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
    MessBox.exec_()

# ---------------------------------------------------------------------------


def getNewVLine(parent=None):
    Result = QtWidgets.QFrame()
    Result.setFrameStyle(QtWidgets.QFrame.VLine | QtWidgets.QFrame.Sunken)
    return Result

# ---------------------------------------------------------------------------


def getNewHLine(parent=None):
    Result = QtWidgets.QFrame()
    Result.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Sunken)
    return Result

# ---------------------------------------------------------------------------


def getNewSpinBoxwithMinMaxVal(MIN, MAX, VAL, parent=None):
    Result = QtWidgets.QSpinBox(parent)
    Result.setMinimum(MIN)
    Result.setMaximum(MAX)
    Result.setValue(VAL)
    return Result

# ---------------------------------------------------------------------------


def moveWindowtoDesktopCenter(window):
    window.setGeometry(
        QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, window.size(),
            QtWidgets.QApplication.desktop().availableGeometry())
    )

# ---------------------------------------------------------------------------


def moveWindowtoFitDesktop(window):
    desk_width = QtWidgets.QApplication.desktop().availableGeometry(window).width()
    desk_height = QtWidgets.QApplication.desktop().availableGeometry(window).height()

    win_width = window.width()
    win_height = window.height()
    win_xPos = window.pos().x()
    win_yPos = window.pos().y()

    if win_xPos < 0:
        win_xPos = 0
    if win_yPos < 0:
        win_yPos = 0

    off_xPos = win_xPos + win_width - desk_width
    off_yPos = win_yPos + win_height - desk_height

    if off_xPos > 0:
        win_xPos = win_xPos - off_xPos

    if off_yPos > 0:
        win_yPos = win_yPos - off_yPos

    window.move(win_xPos, win_yPos)

# ---------------------------------------------------------------------------


def getSysDLDir():
    return QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DownloadLocation)


# ---------------------------------------------------------------------------


def isItURL(textToCheck):
    urlRegex = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
    regex = re.compile(urlRegex, re.IGNORECASE)
    if regex.fullmatch(textToCheck):
        return True
    else:
        return False

    # URL = QtCore.QUrl(textToCheck)
    # return URL.isValid()

# ---------------------------------------------------------------------------


def getURLfromClipboard():
    Clipboard_str = str(QtWidgets.QApplication.clipboard().text(QtGui.QClipboard.Clipboard))

    # print(URL)
    if not isItURL(Clipboard_str):
        return ""

    return Clipboard_str

# ---------------------------------------------------------------------------


def getFileNamefromURL(URL_str):
    # if URL_str.split("/")[-1] == "":
    #     return "unknown"
    # else:
    #     return URL_str.split("/")[-1]

    URL = QtCore.QUrl(URL_str)
    if not URL.isValid():
        return ""

    return URL.fileName()

# ---------------------------------------------------------------------------


def getSizeOfRemoteFile(FileURL):
    try:
        CURL = pycurl.Curl()
        CURL.setopt(CURL.URL, FileURL)
        CURL.setopt(CURL.NOBODY, 1)
        CURL.perform()
        return CURL.getinfo(CURL.CONTENT_LENGTH_DOWNLOAD)
    except pycurl.error:
        return 0

# ---------------------------------------------------------------------------
# https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python


def getReadableFileSize(SizeInBytes):
    if SizeInBytes == 0:
        return "0B"

    SizeName = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(SizeInBytes, 1024)))
    p = math.pow(1024, i)
    s = round(SizeInBytes / p, 2)

    return "{} {}".format(s, SizeName[i])

# ---------------------------------------------------------------------------


def saveList2JSONfile(List, jsonFileName):
    try:
        with open(jsonFileName, "wt") as outFile:
            json.dump(List, outFile)
    except IOError as err:
        showErrorMessBox("saving error", str(err))

# ---------------------------------------------------------------------------


def getListFromJSONfile(jsonFileName):
    try:
        with open(jsonFileName, "rt") as inFile:
            return json.load(inFile)
    except IOError as err:
        showErrorMessBox("loading error", str(err))

# ---------------------------------------------------------------------------


def isFileExistInCurDir(FileName):
    return QtCore.QFileInfo(FileName).exists()
