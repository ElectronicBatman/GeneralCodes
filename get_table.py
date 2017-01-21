import sys
import glob
import serial

from PyQt4 import QtCore, QtGui

table = QtGui.QTableWidget(5, 3)

for row in range(5):
  for col in range(3):
    table.setItem(row, col, QtGui.QTableWidgetItem("(%d, %d)" % (row, col)))

if __name__ == "__main__":
     import sys
     app = QtGui.QApplication(sys.argv)
     MainWindow = QtGui.QMainWindow()
     ui = Ui_MainWindow()
     ui.setupUi(MainWindow)
     MainWindow.show()
     sys.exit(app.exec_())

print("1,0: %s" % table.item(1, 0).text())
