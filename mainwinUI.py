import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):

	def __init__(self, parent= None):
		super(MainWindow, self).__init__(parent)

		self.initUI()

	def initUI(self):
		self.setWindowTitle("Better Download Manager")
		self.setGeometry(50, 50, 640, 480)



def runApp():
	app= QtGui.QApplication(sys.argv)
	
	main_win= MainWindow()
	main_win.showMaximized()

	sys.exit(app.exec_())



if __name__ == "__main__": runApp()

