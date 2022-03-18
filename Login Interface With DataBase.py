# 
# This Humble Project Was Made By Shili Imed 
# The Login Is ( med | 123 )
#
import first, sec, sys
from PyQt5 import QtCore, QtGui, QtWidgets
class Main(object):
	def __init__(self):
		self.Form = QtWidgets.QMainWindow()
		self.first = first.Ui_MainWindow(self.Form)
		
		
	def _hide(self):
		self.Form.hide()
	def Run(self):
		
		self.first.setupUi()
		self.Form.show()
		sys.exit(app.exec_())


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	run = Main()
	run.Run()