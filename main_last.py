import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QListWidgetItem, QMessageBox
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
            QMessageBox.warning(
                self, 'Wrong', 'Incorrect username or password')
            return

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
        self.signupButton.setEnabled(False)
        self.agreeCheckBox.stateChanged.connect(self.checkAll)
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

    def checkAll(self):
        if self.unameLineEdit.text() and self.emailLineEdit.text() and self.pwLineEdit.text() == self.confirmpwLineEdit.text() and self.agreeCheckBox.isChecked():
            self.signupButton.setEnabled(True)
        else:
            self.signupButton.setEnabled(False)

    # 가입 작성을 완료한 후 처리될 기능들의 메서드
    def signUp(self):
        email = self.emailLineEdit.text()
        password = self.pwLineEdit.text()
        if len(password) <= 6:
            QMessageBox.warning(self, 'Check Your Password',
                                'Password is too short')
            return
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
        db.child(userID).child("Profile").set(data)

        login = LoginApp()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class TodoList(QDialog, TodolistUI_Dialog):
    def __init__(self):
        super(TodoList, self).__init__()
        self.setupUi(self)
        self.loadImage()
        self.loadList()
        self.additemButton.clicked.connect(self.addItemList)
        self.deleteitemButton.clicked.connect(self.deleteItemList)
        self.turnoffButton.clicked.connect(self.turnOffItem)
        self.changeitemButton.clicked.connect(self.changeItemList)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    def turnOffItem(self):
        login = LoginApp()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def addItemList(self):
        addlist = AddList()
        widget.addWidget(addlist)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def deleteItemList(self):
        global userID
        todoListWidget = self.todoListWidget
        todoListItems = []
        for i in range(todoListWidget.count()):
            todoListItems.append(todoListWidget.item(i))
        delTodoItems = []
        for item in todoListItems:
            if item.checkState() != 0:
                delTodoItems.append(item)
        # print(delTodoItems)
        for item in delTodoItems:
            # print(item.text().split(" "))
            item_list = item.text().split(" / ")
            # print(item_list)
            self.todoListWidget.takeItem(self.todoListWidget.row(item))
            del_item = db.child(userID).child("Todo_List").child(
                "TO DO").child(item_list[0]).get()
            # print(del_item.val())
            for idx, dict in del_item.val().items():
                del_idx = idx
                for key, val in dict.items():
                    if (key == 'details' and val == item_list[-1]):
                        db.child(userID).child("Todo_List").child(
                            "TO DO").child(item_list[0]).child(del_idx).remove()

        progListWidget = self.inprogressListWidget
        progListItems = []
        for i in range(progListWidget.count()):
            progListItems.append(progListWidget.item(i))
        delProgItems = []
        for item in progListItems:
            if item.checkState() != 0:
                delProgItems.append(item)
        # print(delProgItems)
        for item in delProgItems:
            # print(item.text())
            item_list = item.text().split(" / ")
            self.inprogressListWidget.takeItem(
                self.inprogressListWidget.row(item))
            del_item = db.child(userID).child("Todo_List").child(
                "IN PROGRESS").child(item_list[0]).get()
            # print(del_item.val())
            for idx, dict in del_item.val().items():
                del_idx = idx
                for key, val in dict.items():
                    if (key == 'details' and val == item_list[-1]):
                        db.child(userID).child("Todo_List").child(
                            "IN PROGRESS").child(item_list[0]).child(del_idx).remove()

    def changeItemList(self):
        global userID

        todoListWidget = self.todoListWidget
        todoListItems = []
        for i in range(todoListWidget.count()):
            todoListItems.append(todoListWidget.item(i))
        changeTodoItems = []
        for item in todoListItems:
            if item.checkState() != 0:
                changeTodoItems.append(item)

        progListWidget = self.inprogressListWidget
        progListItems = []
        for i in range(progListWidget.count()):
            progListItems.append(progListWidget.item(i))
        changeProgItems = []
        for item in progListItems:
            if item.checkState() != 0:
                changeProgItems.append(item)

        for item in changeTodoItems:
            self.todoListWidget.takeItem(self.todoListWidget.row(item))
            self.inprogressListWidget.addItem(item)
            item.setCheckState(QtCore.Qt.Unchecked)

            item_list = item.text().split(" / ")
            # print(item_list)
            del_item = db.child(userID).child("Todo_List").child(
                "TO DO").child(item_list[0]).get()
            # print(del_item.val())
            for idx, dict in del_item.val().items():
                del_idx = idx
                for key, val in dict.items():
                    if (key == 'details' and val == item_list[-1]):
                        db.child(userID).child("Todo_List").child(
                            "TO DO").child(item_list[0]).child(del_idx).remove()
                        data = {
                            "importance": item_list[1],
                            "details": item_list[-1]
                        }
                        db.child(userID).child("Todo_List").child(
                            "IN PROGRESS").child(item_list[0]).push(data)

        for item in changeProgItems:
            self.inprogressListWidget.takeItem(
                self.inprogressListWidget.row(item))
            self.todoListWidget.addItem(item)
            item.setCheckState(QtCore.Qt.Unchecked)

            item_list = item.text().split(" / ")
            # print(item_list)
            del_item = db.child(userID).child("Todo_List").child(
                "IN PROGRESS").child(item_list[0]).get()
            # print(del_item.val())
            for idx, dict in del_item.val().items():
                del_idx = idx
                for key, val in dict.items():
                    if (key == 'details' and val == item_list[-1]):
                        db.child(userID).child("Todo_List").child(
                            "IN PROGRESS").child(item_list[0]).child(del_idx).remove()
                        data = {
                            "importance": item_list[1],
                            "details": item_list[-1]
                        }
                        db.child(userID).child("Todo_List").child(
                            "TO DO").child(item_list[0]).push(data)

    def loadImage(self):
        global userID
        image_path = db.child(userID).child(
            "Profile").child("image_path").get()
        self.pixmap = QPixmap(image_path.val()).scaled(
            80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.imageLabel.setPixmap(self.pixmap)

    # 추가하고 삭제한 todo list data들 불러오기
    def loadList(self):
        global userID
        todoData = db.child(userID).child("Todo_List").child("TO DO").get()
        inprogressData = db.child(userID).child(
            "Todo_List").child("IN PROGRESS").get()

        if todoData.each():
            for data in todoData.each():
                item = db.child(userID).child("Todo_List").child(
                    "TO DO").child(data.key()).get()
                for idx, dict in item.val().items():
                    list_item = QListWidgetItem()
                    for key, val in dict.items():
                        if (key == 'importance'):
                            import_item = (val)
                        else:
                            detail_item = (val)
                    list_item.setText(data.key() + " / " +
                                      import_item + " / " + detail_item)
                    list_item.setFlags(list_item.flags() |
                                       QtCore.Qt.ItemIsUserCheckable)
                    list_item.setCheckState(QtCore.Qt.Unchecked)
                    self.todoListWidget.addItem(list_item)

        if inprogressData.each():
            for data in inprogressData.each():
                item = db.child(userID).child("Todo_List").child(
                    "IN PROGRESS").child(data.key()).get()
                for idx, dict in item.val().items():
                    list_item = QListWidgetItem()
                    for key, val in dict.items():
                        if (key == 'importance'):
                            import_item = (val)
                        else:
                            detail_item = (val)
                    list_item.setText(data.key() + " / " +
                                      import_item + " / " + detail_item)
                    list_item.setFlags(list_item.flags() |
                                       QtCore.Qt.ItemIsUserCheckable)
                    list_item.setCheckState(QtCore.Qt.Unchecked)
                    self.inprogressListWidget.addItem(list_item)


class AddList(QDialog, AddListUI_Dialog):
    def __init__(self):
        super(AddList, self).__init__()
        self.setupUi(self)
        self.setImage()  # 초기 workingimageLabel의 이미지 설정하는 메서드
        self.worktypeComboBox.currentIndexChanged.connect(self.setImage)
        self.gobackButton.clicked.connect(self.goBack)
        self.completeadditemButton.setEnabled(False)
        self.detailsLineEdit.textChanged.connect(self.checkDetail)
        self.completeadditemButton.clicked.connect(self.addList)
        widget.setFixedWidth(self.width())
        widget.setFixedHeight(self.height())

    # work type에 따라 아이콘 변경해주는 메서드
    def setImage(self):
        workType = self.worktypeComboBox.currentText()

        if workType == "Study":
            image_path = f"{pathlib.Path()}\\pictures\\studyicon.png"
        elif workType == "Cleaning":
            image_path = f"{pathlib.Path()}\\pictures\\cleaningicon.png"
        elif workType == "Rest":
            image_path = f"{pathlib.Path()}\\pictures\\resticon.png"
        elif workType == "Exercise":
            image_path = f"{pathlib.Path()}\\pictures\\exerciseicon.png"
        else:
            image_path = f"{pathlib.Path()}\\pictures\\readingicon.png"

        source = QPixmap(image_path).scaled(80, 80)
        self.pixmap = QPixmap(image_path).scaled(
            80, 80)
        self.pixmap.fill(QtCore.Qt.transparent)
        qp = QtGui.QPainter(self.pixmap)
        clipPath = QtGui.QPainterPath()
        clipPath.addRoundedRect(QtCore.QRectF(source.rect()), 40, 40)
        qp.setClipPath(clipPath)
        qp.drawPixmap(0, 0, source)
        qp.end()
        self.workimageLabel.setPixmap(self.pixmap)

    def goBack(self):
        todolist = TodoList()
        widget.addWidget(todolist)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # details 란에 아무것도 적지 않으면 add button 클릭 못하게하는 메서드
    def checkDetail(self, detail):
        if detail:
            self.completeadditemButton.setEnabled(True)
        else:
            self.completeadditemButton.setEnabled(False)

    # 작성한 todo List를 firebase에 저장하는 메서드
    def addList(self):
        global userID
        data = {
            "importance": self.importanceComboBox.currentText(),
            "details": self.detailsLineEdit.text()
        }
        db.child(userID).child("Todo_List").child(
            self.processComboBox.currentText()).child(self.worktypeComboBox.currentText()).push(data)

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
