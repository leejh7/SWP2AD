import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from loginUI import LoginUI_Dialog
from createaccUI import CreateAccUI_Dialog
import pyrebase
import pathlib

firebaseConfig = {
    'apiKey': "AIzaSyBM7Sjy_xrrz4y25Uk6-BTRT8r2JRQL7sA",
    'authDomain': "authswp2.firebaseapp.com",
    'databaseURL': "https://authswp2.firebaseio.com",
    'projectId': "authswp2",
    'storageBucket': "authswp2.appspot.com",
    'messagingSenderId': "1091317111314",
    'appId': "1:1091317111314:web:640f415339de82467856cb"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
data = firebase.database()


class LoginApp(QDialog, LoginUI_Dialog):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.signupButton.clicked.connect(self.buttonClicked)
        self.pwLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.clicked.connect(self.login)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    def buttonClicked(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def login(self):
        email = self.unameLineEdit.text()
        password = self.pwLineEdit.text()
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            print('Success')
        except:
            pass


class CreateAcc(QDialog, CreateAccUI_Dialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        self.setupUi(self)
        self.loadButton.clicked.connect(self.loadImage)
        self.gobackButton.clicked.connect(self.buttonClicked)
        self.signupButton.clicked.connect(self.signUp)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    def loadImage(self):
        fname = QFileDialog.getOpenFileName(
            self, "Open File", f"{pathlib.Path().resolve()}\\Images", "All Files (*);;PNG FIles(*.png);;Jpg Files (*.jpg);;Ico Files (*.ico)")

        self.pixmap = QPixmap(fname[0]).scaled(
            80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.imageLabel.setPixmap(self.pixmap)

    def buttonClicked(self):
        login = LoginApp()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def signUp(self):
        email = self.emailLineEdit.text()
        password = self.pwLineEdit.text()
        try:
            user = auth.create_user_with_email_and_password(email, password)
        except:
            pass
        login = LoginApp()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    Form = LoginApp()
    widget.addWidget(Form)
    widget.show()
    sys.exit(app.exec_())
