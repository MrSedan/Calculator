import sys
from calcui import *
import keyboard
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

def ck1():
    ui.lineEdit.setText(ui.lineEdit.text()+'1')

def ck2():
    ui.lineEdit.setText(ui.lineEdit.text()+'2')

def ck3():
    ui.lineEdit.setText(ui.lineEdit.text()+'3')

def ck4():
    ui.lineEdit.setText(ui.lineEdit.text()+'4')

def ck5():
    ui.lineEdit.setText(ui.lineEdit.text()+'5')

def ck6():
    ui.lineEdit.setText(ui.lineEdit.text()+'6')

def ck7():
    ui.lineEdit.setText(ui.lineEdit.text()+'7')

def ck8():
    ui.lineEdit.setText(ui.lineEdit.text()+'8')

def ck9():
    ui.lineEdit.setText(ui.lineEdit.text()+'9')

def ck0():
    ui.lineEdit.setText(ui.lineEdit.text()+'0')

def ckm():
    try:
        text = ui.lineEdit.text()
        if text[len(text)-1] not in ['-','+']: ui.lineEdit.setText(ui.lineEdit.text()+'-')
    except:
        pass

def ckp():
    try:
        text = ui.lineEdit.text()
        if text[len(text) - 1] not in ['-', '+']: ui.lineEdit.setText(ui.lineEdit.text() + '+')
    except:
        pass

def ckd():
    try:
        text = ui.lineEdit.text()
        if text[len(text) - 1] not in ['-', '+','.','/','*']: ui.lineEdit.setText(ui.lineEdit.text() + '.')
    except:
        pass

def ckpod():
    try:
        text = ui.lineEdit.text()
        if text[len(text) - 1] not in ['-', '+','.','/','*']: ui.lineEdit.setText(ui.lineEdit.text() + '/')
    except:
        pass

def cku():
    try:
        text = ui.lineEdit.text()
        if text[len(text) - 1] not in ['-', '+','.','/','*']: ui.lineEdit.setText(ui.lineEdit.text() + '*')
    except:
        pass

def ckc():
    try:
        i = len(ui.lineEdit.text())-1
        while ui.lineEdit.text()[i] not in ['-', '+','.','/','*']:
            ui.lineEdit.backspace()
            i-=1
    except:
        pass

def ckce():
    try:
        ui.lineEdit.setText('')
    except:
        pass

def ckv():
    try:
        ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
    except:
        pass


def bp():
    ui.lineEdit.backspace()
ui.lineEdit.setReadOnly(True)
ui.pushButton_9.clicked.connect(ck1)
ui.pushButton_6.clicked.connect(ck2)
ui.pushButton_10.clicked.connect(ck3)
ui.pushButton_7.clicked.connect(ck4)
ui.pushButton_5.clicked.connect(ck5)
ui.pushButton_8.clicked.connect(ck6)
ui.pushButton.clicked.connect(ck7)
ui.pushButton_2.clicked.connect(ck8)
ui.pushButton_3.clicked.connect(ck9)
ui.pushButton_13.clicked.connect(ck0)
ui.pushButton_4.clicked.connect(ckm)
ui.pushButton_11.clicked.connect(ckp)
ui.pushButton_12.clicked.connect(ckv)
ui.pushButton_14.clicked.connect(ckd)
ui.pushButton_15.clicked.connect(cku)
ui.pushButton_16.clicked.connect(ckpod)
ui.pushButton_17.clicked.connect(bp)
ui.pushButton_18.clicked.connect(ckc)
ui.pushButton_19.clicked.connect(ckce)


keyboard.add_hotkey('1',ck1)
keyboard.add_hotkey('2',ck2)
keyboard.add_hotkey('3',ck3)
keyboard.add_hotkey('4',ck4)
keyboard.add_hotkey('5',ck5)
keyboard.add_hotkey('6',ck6)
keyboard.add_hotkey('7',ck7)
keyboard.add_hotkey('8',ck8)
keyboard.add_hotkey('9',ck9)
keyboard.add_hotkey('0',ck0)
keyboard.add_hotkey('-',ckm)
keyboard.add_hotkey('+',ckp)
keyboard.add_hotkey('=',ckv)
keyboard.add_hotkey('.',ckd)
keyboard.add_hotkey('*',cku)
keyboard.add_hotkey('Enter',ckv)
keyboard.add_hotkey('Backspace', bp)


sys.exit(app.exec_())
