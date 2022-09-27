from PyQt4 import QtGui
from PyQt4 import QtCore
from recommendations import *
import logging

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(848, 623)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, -10, 701, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 641, 491))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        '''self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 360, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))'''
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(670, 180, 171, 41))

        #self.pushButton.clicked.connect(self.runner)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setUnderline(False)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(670, 230, 171, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton_3 = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(670, 280, 161, 41))
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)   
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "RECOMMENDATION SYSTEM", None))
        self.label_2.setPixmap(QtGui.QPixmap("yo1.jpg"))
        self.commandLinkButton.setText(_translate("MainWindow", "movies", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "recommendations", None))
        self.commandLinkButton_3.setText(_translate("MainWindow", "and more....", None))



class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'a' and
            self.textPass.text() == 'a'):
            self.accept()
            
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

            
class Window(object):
    def setup(self,Dialog):
        #super(Window, self).__init__(parent)
        #layout = QtGui.QFormLayout() 
        #self.l1=QtGui.QLabel("Name")

        #layout.addWidget(self.l1) 
        #self.nm = QtGui.QLineEdit(self)
         
        #self.btn = QtGui.QPushButton('Enter', self)
       # self.btn.clicked.connect(self.recommend)
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.nm = QtGui.QLabel(Dialog)
        self.nm.setGeometry(QtCore.QRect(90, 80, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nm.setFont(font)
        self.nm.setObjectName(_fromUtf8("nm"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.it1 = QtGui.QComboBox(Dialog)
        self.it1.setGeometry(QtCore.QRect(160, 120, 121, 22))
        self.it1.setObjectName(_fromUtf8("it1"))
        self.it1.addItem(_fromUtf8(""))
        self.it1.addItem(_fromUtf8(""))
        self.it1.addItem(_fromUtf8(""))
        self.it1.addItem(_fromUtf8(""))
        self.it1.addItem(_fromUtf8(""))
        self.it1.addItem(_fromUtf8(""))
        self.it2 = QtGui.QComboBox(Dialog)
        self.it2.setGeometry(QtCore.QRect(160, 160, 121, 22))
        self.it2.setObjectName(_fromUtf8("it2"))
        self.it2.addItem(_fromUtf8(""))
        self.it2.addItem(_fromUtf8(""))
        self.it2.addItem(_fromUtf8(""))
        self.it2.addItem(_fromUtf8(""))
        self.it2.addItem(_fromUtf8(""))
        self.it2.addItem(_fromUtf8(""))
        self.m1 = QtGui.QLabel(Dialog)
        self.m1.setGeometry(QtCore.QRect(80, 120, 47, 13))
        self.m1.setObjectName(_fromUtf8("m1"))
        self.m2 = QtGui.QLabel(Dialog)
        self.m2.setGeometry(QtCore.QRect(80, 160, 47, 13))
        self.m2.setObjectName(_fromUtf8("m2"))
        self.btn = QtGui.QPushButton(Dialog)
        self.btn.setGeometry(QtCore.QRect(100, 210, 71, 23))
        self.btn.setObjectName(_fromUtf8("btn"))

        self.btn.clicked.connect(self.recommend)
        self.rat1 = QtGui.QSpinBox(Dialog)
        self.rat1.setGeometry(QtCore.QRect(310, 120, 42, 22))
        self.rat1.setMinimum(1)
        self.rat1.setMaximum(5)
        self.rat1.setObjectName(_fromUtf8("r1"))
        self.rat2 = QtGui.QSpinBox(Dialog)
        self.rat2.setGeometry(QtCore.QRect(310, 160, 42, 22))
        self.rat2.setMinimum(1)
        self.rat2.setMaximum(5)
        self.rat2.setObjectName(_fromUtf8("rat2"))
        self.colon = QtGui.QLabel(Dialog)
        self.colon.setGeometry(QtCore.QRect(290, 120, 16, 16))
        self.colon.setObjectName(_fromUtf8("colon"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 160, 16, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Recommendation System", None))
        self.nm.setText(_translate("Dialog", "Name", None))
        self.it1.setItemText(0, _translate("Dialog", "Lady in the Water", None))
        self.it1.setItemText(1, _translate("Dialog", "Snakes on a Plane", None))
        self.it1.setItemText(2, _translate("Dialog", "Just My Luck", None))
        self.it1.setItemText(3, _translate("Dialog", "Superman Returns", None))
        self.it1.setItemText(4, _translate("Dialog", "You, Me and Dupree", None))
        self.it1.setItemText(5, _translate("Dialog", "The Night Listener", None))
        self.it2.setItemText(0, _translate("Dialog", "Lady in the Water", None))
        self.it2.setItemText(1, _translate("Dialog", "Snakes on a Plane", None))
        self.it2.setItemText(2, _translate("Dialog", "Just My Luck", None))
        self.it2.setItemText(3, _translate("Dialog", "Superman Returns", None))
        self.it2.setItemText(4, _translate("Dialog", "You, Me and Dupree", None))
        self.it2.setItemText(5, _translate("Dialog", "The Night Listener", None))
        self.m1.setText(_translate("Dialog", "Movie 1:", None))
        self.m2.setText(_translate("Dialog", "Movie 2:", None))
        self.btn.setText(_translate("Dialog", "Get ", None))
        self.colon.setText(_translate("Dialog", ":", None))
        self.label_2.setText(_translate("Dialog", ":", None))

    def recommend(self):
        critics.update({'self.lineEdit.text()':{self.it1.currentText() :self.rat1.value(),self.it2.currentText() :self.rat2.value()}})
        crit=critics.copy()
        self.movies=transformPrefs(crit)
        self.answer=topMatches(self.movies,self.it1.currentText())
        msg=QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Thank you for choosing movies!! ")
        msg.setInformativeText("Now, Click on Ok button to get recommendations") 
        msg.setWindowTitle("Recommendation System")
        msg.setDetailedText("This project is created by Prabhjeet Singh and Shantanu Sharma. It gives you movies of your tastes.")
        msg.setStandardButtons(QtGui.QMessageBox.Ok )
        msg.buttonClicked.connect(self.msgbtn)
        retval=msg.exec_()
        print ("value of pressed message box button:", retval )
        #print(answer)
     
    def msgbtn(self):
        #sys.exit(app.exec_()) 
        for i in self.answer:
            print(i)
            
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        Dialog = QtGui.QDialog()
        ui = Window()
        ui.setup(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
        
    
