from PySide2 import QtWidgets

import ui
import metodos

class MyQtApp(ui.Ui_background, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Application - Build 1.0")
        self.PB_result.clicked.connect(lambda: self.resolve(self.input_data(), self.RB_trapezium.isChecked(), self.RB_Sone.isChecked(), self.RB_Stwo.isChecked()))

    def resolve(self, flag, trapezium_ck, sone_ck, stwo_ck):
        if flag:
            if trapezium_ck:
                self.answer = metodos.calculoTrapezio(self.equation, self.subit, self.lower, self.upper)
            if sone_ck:
                self.answer = metodos.calculoPrimeiraSimpson(self.equation, self.subit, self.lower, self.upper)
            if stwo_ck:
                self.answer = metodos.calculoSegundaSimpson(self.equation, self.subit, self.lower, self.upper)
            self.Answer.setText("Answer: "+ str(self.answer))
            

    def input_data(self):
        flag = True
        temp = self.Up_line.text()
        if temp:
            self.upper = float(temp)
        else:
            flag = False
        
        temp = self.Lw_line.text()
        if temp:
            self.lower = float(temp)
        else:
            flag = False

        temp = self.Sub_line.text()
        if temp:
            self.subit = int(temp)
        else:
            flag = False

        temp = self.Eqt_line.text()
        if temp:
            self.equation = temp
        else:
            flag = False

        if flag:
            print(self.upper)
            print(self.lower)
            print(self.subit)
            print(self.equation)

        return flag


app = QtWidgets.QApplication()
qt_app = MyQtApp()
qt_app.show()
app.exec_()