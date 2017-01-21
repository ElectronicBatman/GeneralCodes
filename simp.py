import sys
from PyQt4 import QtGui



from PyQt4 import QtCore, QtGui
import random
app = QtGui.QApplication(sys.argv)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, argList):
        super(MainWindow, self).__init__()
        self.argList=argList

        mainQWidget = QtGui.QWidget()
        mainLayout=QtGui.QVBoxLayout()

        for i in range(len(self.argList)):
            exec( 'myGroupBox'+str(i)+'= QtGui.QGroupBox() ' )
            exec( 'myLayout'+str(i)+' = QtGui.QHBoxLayout()' )                   

            exec( 'label'+str(i)+'=QtGui.QLabel("Name '+str(self.argList[i])+': ")' )
            exec( 'label'+str(i)+'.setFixedWidth(100)' )
            exec( 'self.myLineEdit'+str(i)+'=QtGui.QLineEdit()' )
            exec( 'self.myLineEdit'+str(i)+'.setText("'+str(random.random())+'")' )


            exec( 'myLayout'+str(i)+'.addWidget(label'+str(i)+')' )
            exec( 'myLayout'+str(i)+'.addWidget(self.myLineEdit'+str(i)+', QtCore.Qt.AlignRight)' )

            exec( 'myGroupBox'+str(i)+'.setLayout(myLayout'+str(i)+')' )
            exec( 'mainLayout.addWidget(myGroupBox'+str(i)+')' )

        ButtonBox = QtGui.QGroupBox()
        ButtonsLayout = QtGui.QHBoxLayout()

        Button_01 = QtGui.QPushButton("Close")
        Button_01.clicked.connect(self.close)

        Button_02 = QtGui.QPushButton("Print")
        Button_02.clicked.connect(self.printOut)

        ButtonsLayout.addWidget(Button_01)
        ButtonsLayout.addWidget(Button_02)

        ButtonBox.setLayout(ButtonsLayout)
        mainLayout.addWidget(ButtonBox)

        mainQWidget.setLayout(mainLayout)
        self.setCentralWidget(mainQWidget)


    def printOut(self):
        for i in range(len(self.argList)):
            exec( 'print self.myLineEdit'+str(i)+'.text()' )
    def close(self):
        sys.exit()


myList=['One','Two','Tree','Four','Five','Six','Seven','Eight']
window = MainWindow(myList)
window.show()
window.resize(480,320)
sys.exit(app.exec_())

if __name__ == '__main__':
   window()
