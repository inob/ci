import sys
from PyQt5 import QtWidgets
import Login

class ExampleApp(QtWidgets.QMainWindow, Login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #Инициализируем дизайн

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.shop()
    app.exec_()

if __name__ == '__main__':
    main()