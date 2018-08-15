from PyQt5 import QtCore


class AppSettings(QtCore.QSettings):

    def __init__(self, organizationName, applicationName):
        super(AppSettings, self).__init__(organizationName, applicationName)

# ************************************************************************

    def add2AppSettings(self, Key2Add, Value2Add):
        self.setValue(Key2Add, Value2Add)

# ************************************************************************

    def getValFromAppSettings(self, Key2Get, DefaultVal=None, ReturnType=None):

        if ReturnType is None:
            return self.value(Key2Get, DefaultVal)
        else:
            return self.value(Key2Get, DefaultVal, type=ReturnType)


# ************************************************************************

    def isKeyExistInAppSettings(self, Key2Check):
        return self.contains(Key2Check)
