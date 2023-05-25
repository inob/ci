import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import requests
from bs4 import BeautifulSoup
from util import read_text, primfacs, is_prime, get_uneven, test_Rabin_Miller, s_s, get_prime_number_in_range
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtGui
from math import gcd

class Maestro(QDialog):
    def __init__(self):
        super(Maestro,self).__init__()
        loadUi("maestro.ui",self)
        widget.setFixedWidth(470)
        widget.setFixedHeight(700)
        self.pushButton.clicked.connect(self.getStudent)
        self.pushButton_2.clicked.connect(self.exit)

    def exit(self):
        login = Login()
        widget.addWidget(login)
        widget.setFixedWidth(600)
        widget.setFixedHeight(700)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def getStudent(self):
        what = self.comboBox.currentText()
        whoo = self.lineEdit.text()
        print(what)
        print(whoo)
        out = ""
        if "туде" in what:
            print("Ст")
            page = requests.post('http://127.0.0.1/Mem/getGroup.php', data={'what':"student", 'whoo':whoo})
            soup = BeautifulSoup(page.content, "html5lib")
            print(soup.text)
            #self.label_2.setText(soup.text)

            label_text = QLabel(soup.text)
            label_text.setWordWrap(True)
            self.scrollArea.setWidget(label_text)

        elif "пп" in what:
            print("пп")
            page = requests.post('http://127.0.0.1/Mem/getGroup.php', data={'what':"group", 'whoo':whoo})
            soup = BeautifulSoup(page.content, "html5lib")
            print(soup.text)
            stud = soup.text.split("|")
            out+=f"Количество оценок по группе: {len(stud)-1}\n\n"
            for i in stud:
                out+= f"{i}\n"
            label_text = QLabel(out)
            label_text.setWordWrap(True)
            self.scrollArea.setWidget(label_text)
        
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Login.ui",self)
        self.password 
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.auth.clicked.connect(self.loginF)
        self.pushButton_3.clicked.connect(self.gotocreate)
    
    def loginF(self):
        if self.login.text() and self.password.text():
            login = self.login.text()
            password = self.password.text()
            page = requests.post('http://127.0.0.1/Mem/safe.php', data={'login':login, 'password':password})
            soup = BeautifulSoup(page.content, "html5lib")
            print(soup.text)
            global UserName
            global UserGroup
            UserName = login
            print(UserName)
            self.label.setText(soup.text)
            if "Maestro" in soup.text:
                self.gotoMaestro()
            if "-" in soup.text:
                UserGroup = soup.text
                print(UserGroup)
                self.gotoChoose()

    def gotoMaestro(self):
        maest = Maestro()
        widget.addWidget(maest)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

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
        self.ktest.clicked.connect(self.goTest)
    
    def goTest(self):
        test = k_test()
        widget.addWidget(test)
        widget.setCurrentIndex(widget.currentIndex()+1)

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

class k_test(QDialog):
    def __init__(self):
        super(k_test,self).__init__()
        loadUi("ktest.ui",self)
        widget.setFixedWidth(707)
        widget.setFixedHeight(735)
        print(UserName)
        self.label.setText(UserName)
        self.pushButton.clicked.connect(self.generate)
        self.pushButton_2.clicked.connect(self.complete)
        self.pushButton_3.clicked.connect(self.goBack)
    
    def goBack(self):
        choosee = Choose()
        widget.addWidget(choosee)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedWidth(600)
        widget.setFixedHeight(700)

    def complete(self):
        itog = 0
        if self.radioButton.isChecked(): itog+=1
        if self.radioButton_7.isChecked(): itog+=1
        if self.radioButton_3.isChecked(): itog+=1
        if self.lineEdit_3.text() == "1": itog+=1

        p = int(self.dannie_4.text())
        a = int(self.dannie_5.text())
        nod, jac, ans, otvet = s_s(p,a)

        if str(jac) == self.lineEdit_2.text(): itog+=1

        x = int(self.dannie_9.text())
        ls = max(primfacs(x))
        if str(ls) == self.lineEdit_8.text(): itog+=1

        print(f"{itog}/6")
        grade = round((10/6)*itog)
        page = requests.post('http://127.0.0.1/Mem/grade.php', data={'person':UserName, 'grade':grade, 'group':UserGroup})
        soup = BeautifulSoup(page.content, "html5lib")
        print(soup.text)
        
        self.goBack()


    def generate(self):
        num = get_uneven(50,270)
        numA = 2
        self.dannie_4.setText(str(num))
        for i in range(3, num):
            if gcd(i, num) == 1:
                self.dannie_5.setText(str(i))
                numA = i
                break
        

        prime1, prime2, prime3, prime4 = get_prime_number_in_range(2100, 39999),get_prime_number_in_range(3000, 40000), get_prime_number_in_range(3000, 4000),get_prime_number_in_range(3000, 40000)
        self.dannie.setText(str(prime1))
        self.dannie_10.setText(str(prime2))
        self.dannie_6.setText(str(prime3))
        self.dannie_8.setText(str(prime4))
        self.dannie_7.setText("4")
        temp = get_uneven(1001,1400)
        self.dannie_9.setText(str(temp))


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
            self.result.setText("Верно.")
        else:
            self.result.setText("Неверно.")

        

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

    def solve(self): 
        p = int(self.lineEdit.text())
        a = int(self.lineEdit_2.text())
        nod, jac, ans, otvet = s_s(p,a)
        if "прост" in otvet: otvet =  " псевдопростым"
        else: otvet = " составным"
        self.label_5.setText(f"""<p>НОД введенных чисел равен {nod}</p>
                                <p>({a}/{p}) = {jac}</p>
                                <p>{a}<sup>({p}-1)/2</sup> &equiv; {ans}(mod {p})</p>
                                <p>Следовательно, число является {otvet}</p>""")

    def GenerateValue(self):
        num = get_uneven(50,270)
        numA = 2
        self.chisloP.setText(str(num))
        for i in range(3, num):
            if gcd(i, num) == 1:
                self.chisloA.setText(str(i))
                numA = i
                break

    def checkValue(self): 
        p = int(self.chisloP.text())
        a = int(self.chisloA.text())
        nod, jac, ans, otvet = s_s(p,a)
        ansS = int(self.lineEdit_3.text())
        ansR = int(self.lineEdit_4.text())
        if ansS != jac or ansR != ans: self.result.setText("Неверно.")
        else: self.result.setText("Верно.")
        


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
        p = int(self.lineEdit.text())
        a = int(self.lineEdit_2.text())
        if p%2==0: 
            self.label_5.setText(f"<p>Число должно быть нечетным</p>")
            return 0
            
        ans,text,trash = test_Rabin_Miller(p, a)
        if 2 < a < p - 2:
            temp = primfacs(p-1)
            text_2 = ""
            for i in temp: text_2+=f"{int(i)}, "
            gotText = f"""<p>Число {p-1} разложим как {text_2[:-2]}</p>
                            <p>Следовательно:</p>
                                        {text}"""

            if ans: 
                self.label_5.setText(f"{gotText}<p>Число, вероятно всего, простое.</p>")
                self.label_5.setWordWrap(True)
            else: 
                self.label_5.setText(f"{gotText}<p>Число составное.</p>")
                self.label_5.setWordWrap(True)
            
                
            

    def GenerateValue(self): 
        num = get_uneven(50,270)
        numA = 2
        self.chisloP.setText(str(num))
        for i in range(3, num):
            if gcd(i, num) == 1:
                self.chisloA.setText(str(i))
                numA = i
                break

    def checkValue(self): 
        p = int(self.chisloP.text())
        a = int(self.chisloA.text())
        x,y,ans = test_Rabin_Miller(p,a)
        d,r = ans

        ansR = int(self.lineEdit_3.text())
        ansD = int(self.lineEdit_4.text())

        if ansR != r or ansD != d:
            self.result1.setText(f"Неверно !")
            self.result1.setWordWrap(True)
        else:
            self.result1.setText(f"Верно !")
            self.result1.setWordWrap(True)

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
            group = self.group.text()
            page = requests.post('http://127.0.0.1/Mem/registration.php', data={'login':login, 'password':password, 'email':email, 'group':group})
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
widget.setWindowTitle("CryptoCifra")
widget.show()
app.exec_()  