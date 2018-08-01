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


def getVLine(parent=None):
    Result = QtWidgets.QFrame()
    Result.setFrameStyle(QtWidgets.QFrame.VLine | QtWidgets.QFrame.Sunken)
    return Result

# ---------------------------------------------------------------------------


def getHLine(parent=None):
    Result = QtWidgets.QFrame()
    Result.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Sunken)
    return Result

# ---------------------------------------------------------------------------


def getSpinBoxwithMinMaxVal(MIN, MAX, VAL, parent=None):
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

    
