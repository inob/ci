import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import requests
from bs4 import BeautifulSoup
from util import read_text, primfacs, is_prime
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
from math import gcd

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Login.ui",self)
        self.auth.clicked.connect(self.loginF)
        self.pushButton_3.clicked.connect(self.gotocreate)
    
    def loginF(self):
        if self.login.text() and self.password.text():
            login = self.login.text()
            password = self.password.text()
            page = requests.post('http://127.0.0.1/Mem/safe.php', data={'login':login, 'password':password})
            soup = BeautifulSoup(page.content, "html5lib")
            print(soup.text)
            self.label.setText(soup.text)
            if "good" in soup.text:
                self.gotoChoose()

    def gotocreate(self):
        createacc = Registr()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoChoose(self):
        choosee = Choose()
        widget.addWidget(choosee)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Choose(QDialog):
    def __init__(self):
        super(Choose,self).__init__()
        loadUi("Choose.ui",self)
        self.buttonFerma.clicked.connect(self.goFerma)

    def goFerma(self):
        ferma = Ferma()
        widget.addWidget(ferma)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Ferma(QDialog):
    def __init__(self):
        super(Ferma,self).__init__()
        loadUi("Ferma.ui",self)
        widget.setFixedWidth(707)
        widget.setFixedHeight(735)
        text = read_text('Ferm_Theory.html')
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        self.scrollArea.setWidget(label_text)
        self.pushButton.clicked.connect(self.answer)

    def answer(self):
        n = int(self.lineEdit.text())
        a = int(self.lineEdit_2.text())
        if gcd(n,a)==1 and n>=2 and a >= 2:
            n-=1
            x = [int(x) for x in primfacs(n)]
            num = "("*len(x) + f"{a}"
            for i in x:
                num+=f")<sup>{i}</sup>"
            print(x)
            if is_prime(n+1):    
                self.label_5.setText(f"""<p> {a}<sup>{n}</sup> &equiv; {num} &equiv; 1(mod {n+1})</p>
                                         <p> Число {n+1}, вероятнее всего, <b>простое.</b>""")

                self.label_5.setWordWrap(True)
            else:
                self.label_5.setText(f"""<p> {a}<sup>{n}</sup> &equiv; {num} &ne; 1(mod {n+1})</p>
                                         <p> Число {n+1} - <b>составное.</b>""")
                self.label_5.setWordWrap(True)
        else:
            label_5 = QLabel("Числа не взаимно простые.")


class SV(QDialog):
    def __init__(self):
        super(Ferma,self).__init__()
        loadUi("Ferma.ui",self)
        widget.setFixedWidth(707)
        widget.setFixedHeight(735)
        text = read_text('MR_Theory.html')
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        self.scrollArea.setWidget(label_text)

class Miller(QDialog):
    def __init__(self):
        super(Ferma,self).__init__()
        loadUi("Ferma.ui",self)
        widget.setFixedWidth(707)
        widget.setFixedHeight(735)
        text = read_text('SV_Theory.html')
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        self.scrollArea.setWidget(label_text)

class Registr(QDialog):
    def __init__(self):
        super(Registr,self).__init__()
        loadUi("Registration.ui",self)
        self.signupbutton.clicked.connect(self.createAcc)
        self.auth_back.clicked.connect(self.authBack)

    def authBack(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def createAcc(self):
        if self.login.text() and self.password.text():
            login = self.login.text()
            password = self.password.text()
            cpassword = self.confirmpass.text()
            email = self.email.text()
            page = requests.post('http://127.0.0.1/Mem/registration.php', data={'login':login, 'password':password, 'email':email})
            soup = BeautifulSoup(page.content, "html5lib")
            print(soup.text)
            if soup.text: self.authBack() 
            else: self.label_5.setText("Регистрация не прошла !")




app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(960)
widget.setFixedHeight(620)
widget.show()
app.exec_()  