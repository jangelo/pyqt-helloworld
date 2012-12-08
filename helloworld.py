"""
    Simple example of using pyqt, ui file and custom stylesheet.
"""
import sys
from PyQt4 import QtGui, QtCore, uic
 
class HelloworldApp(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        f = open('resources/darkorange.stylesheet', 'r')
        self.styleData = f.read()
        f.close()

        self.ui = uic.loadUi('helloworld.ui')
        self.ui.setStyleSheet(self.styleData)
        self.ui.show()
        
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), submitClicked)
 
def submitClicked():
    """ Called with pushButton is clicked. Updates label with text from editline. """
    value = win.ui.lineEdit.text()
    win.ui.label.setText('Hello  ' + str(value))
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle('plastique')
    win = HelloworldApp()
    sys.exit(app.exec_())