from PyQt5 import QtWidgets


def createAction(parent=None, actTitle="New Action", actShortcut="", actTip="", actTriger=None):

    Result = QtWidgets.QAction(actTitle, parent)
    Result.setShortcut(actShortcut)
    Result.setToolTip(actTip)
    Result.setStatusTip(actTip)
    if actTriger:
        Result.triggered.connect(actTriger)

    return Result
