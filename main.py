import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from loginUI import LoginUI_Dialog
from createaccUI import CreateAccUI_Dialog
from todolistUI import TodolistUI_Dialog
from addlistUI import AddListUI_Dialog
import pyrebase
import pathlib

firebaseConfig = {
    "apiKey": "AIzaSyBM7Sjy_xrrz4y25Uk6-BTRT8r2JRQL7sA",
    "authDomain": "authswp2.firebaseapp.com",
    "databaseURL": "https://authswp2-default-rtdb.firebaseio.com",
    "projectId": "authswp2",
    "storageBucket": "authswp2.appspot.com",
    "messagingSenderId": "1091317111314",
    "appId": "1:1091317111314:web:640f415339de82467856cb"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()


class LoginApp(QDialog, LoginUI_Dialog):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.signupButton.clicked.connect(self.signUp)
        self.pwLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.clicked.connect(self.login)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    def signUp(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def login(self):
        email = self.emailLineEdit.text()
        password = self.pwLineEdit.text()
        try:
            login = auth.sign_in_with_email_and_password(email, password)
        except:
            pass

        global userID
        userID = email.split('@')[0]
        # 로그인 승인시 TodoList page로 넘어가기
        todolist = TodoList()
        widget.addWidget(todolist)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog, CreateAccUI_Dialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        self.setupUi(self)
        self.pwLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpwLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loadButton.clicked.connect(self.loadImage)
        self.gobackButton.clicked.connect(self.goBack)
        self.signupButton.clicked.connect(self.signUp)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    # 사용자 프로필 이미지 설정해주기 위한 메서드
    def loadImage(self):
        self.fname = QFileDialog.getOpenFileName(
            self, "Open File", f"{pathlib.Path().resolve()}\\Images", "All Files (*);;PNG FIles(*.png);;Jpg Files (*.jpg);;")
        self.pixmap = QPixmap(self.fname[0]).scaled(
            80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.imageLabel.setPixmap(self.pixmap)

    def goBack(self):
        login = LoginApp()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # 가입 작성을 완료한 후 처리될 기능들의 메서드
    def signUp(self):
        email = self.emailLineEdit.text()
        password = self.pwLineEdit.text()
        try:
            user = auth.create_user_with_email_and_password(email, password)
        except:
            pass

        userID = self.emailLineEdit.text().split('@')[0]

        # 프로필 이미지로 설정한 이미지를 firebase storage에 저장
        cloudfilename = f"{userID}/{self.fname[0].split('/')[-1]}"
        storage.child(cloudfilename).put(self.fname[0])

        # 프로필 이름과 이미지 명을 firebase realtime database에 저장
        data = {"name": self.unameLineEdit.text(), "image_path": self.fname[0]}
        db.child(userID).child("profile").set(data)

        login = LoginApp()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class TodoList(QDialog, TodolistUI_Dialog):
    def __init__(self):
        super(TodoList, self).__init__()
        self.setupUi(self)
        self.loadImage()
        self.additemButton.clicked.connect(self.addItemList)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    def addItemList(self):
        addlist = AddList()
        widget.addWidget(addlist)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loadImage(self):
        global userID
        image_path = db.child(userID).child(
            "profile").child("image_path").get()
        self.pixmap = QPixmap(image_path.val()).scaled(
            80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.imageLabel.setPixmap(self.pixmap)


class AddList(QDialog, AddListUI_Dialog):
    def __init__(self):
        super(AddList, self).__init__()
        self.setupUi(self)
        self.gobackButton.clicked.connect(self.goBack)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    def goBack(self):
        todolist = TodoList()
        widget.addWidget(todolist)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    userID = ''
    widget = QtWidgets.QStackedWidget()
    Form = LoginApp()
    widget.addWidget(Form)
    widget.show()
    sys.exit(app.exec_())
