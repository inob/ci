import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import requests
from bs4 import BeautifulSoup
from util import read_text, primfacs, is_prime, get_uneven, get_miller
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
        self.buttonSV.clicked.connect(self.goSV)
        self.buttonMillera.clicked.connect(self.goMR)
    
    def goSV(self):
        s_shtrassena = SV()
        widget.addWidget(s_shtrassena)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goMR(self):
        m_rabina = Miller()
        widget.addWidget(m_rabina)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        self.pushButtonDaOno.clicked.connect(self.generated_num)
        self.checkAns.clicked.connect(self.check)
        self.buttonBack.clicked.connect(self.goBack)

    def goBack(self):
        choosee = Choose()
        widget.addWidget(choosee)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(600)
        widget.setFixedHeight(700)

    def generated_num(self):
        num = get_uneven(50,270)
        numA = 2
        self.chisloP.setText(str(num))
        for i in range(3, num):
            if gcd(i, num) == 1:
                self.chisloA.setText(str(i))
                numA = i
                break
    
    def check(self):
        answ = int(self.lineEdit_3.text())
        p = int(self.chisloP.text())
        a = int(self.chisloA.text())
        cc = (a**(p-1))%p
        if  answ == cc:
            self.result.setText("Верно")
        else:
            self.result.setText("Неверно")

        

    def answer(self):
        n = int(self.lineEdit.text())
        a = int(self.lineEdit_2.text())
        cc = (a**(n-1))%n
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
                self.label_5.setText(f"""<p> {a}<sup>{n}</sup> &equiv; {num} &equiv; {cc}(mod {n+1}) &ne; 1(mod {n+1})</p>
                                         <p> Число {n+1} - <b>составное.</b>""")
                self.label_5.setWordWrap(True)
        else:
            self.label_5.setText(f"""<p> Числа не взаимно простые.</p>""")


class SV(QDialog):
    def __init__(self):
        super(SV,self).__init__()
        loadUi("s_shtrassen.ui",self)
        widget.setFixedWidth(707)
        widget.setFixedHeight(735)
        text = read_text('Shtrassen_Theory.html')
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        self.scrollArea.setWidget(label_text)
        self.reshit.clicked.connect(self.solve)
        self.ButtonGenerated.clicked.connect(self.GenerateValue)
        self.check_shtrassen.clicked.connect(self.checkValue)
        self.buttonBack.clicked.connect(self.goBack)

    def goBack(self):
        choosee = Choose()
        widget.addWidget(choosee)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(600)
        widget.setFixedHeight(700)

    def solve(self): pass

    def GenerateValue(self): pass

    def checkValue(self): pass

class Miller(QDialog):
    def __init__(self):
        super(Miller,self).__init__()
        loadUi("Miller.ui",self)
        widget.setFixedWidth(707)
        widget.setFixedHeight(735)
        text = read_text('Miller_Theory.html')
        label_text = QLabel(text)
        label_text.setWordWrap(True)
        self.scrollArea.setWidget(label_text)
        self.reshit.clicked.connect(self.solve)
        self.ButtonGenerated.clicked.connect(self.GenerateValue)
        self.check_shtrassen.clicked.connect(self.checkValue)
        self.buttonBack.clicked.connect(self.goBack)

    def goBack(self):
        choosee = Choose()
        widget.addWidget(choosee)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(600)
        widget.setFixedHeight(700)


    def solve(self):
        get_miller(81)

    def GenerateValue(self): pass

    def checkValue(self): pass
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
widget.setFixedWidth(600)
widget.setFixedHeight(700)
widget.show()
app.exec_()  