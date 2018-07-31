from PyQt5 import QtWidgets, QtCore


# ---------------------------------------------------------------------------

def getAction(parent=None, actTitle="New Action", actShortcut="", actTip="", actTriger=None):

    Result = QtWidgets.QAction(actTitle, parent)
    Result.setShortcut(actShortcut)
    Result.setToolTip(actTip)
    Result.setStatusTip(actTip)
    if actTriger:
        Result.triggered.connect(actTriger)

    return Result

# ---------------------------------------------------------------------------


def getBuddyLabel(title, buddy, parent=None):
    Result = QtWidgets.QLabel(title, parent)
    Result.setBuddy(buddy)

    return Result

# ---------------------------------------------------------------------------


def getSysDLDir():
    return QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DownloadLocation)

# ---------------------------------------------------------------------------
