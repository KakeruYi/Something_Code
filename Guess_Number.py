import numpy as np
from PyQt6 import QtWidgets
import sys
import random

count = 0
boundary_num = 0
answer = 0

def reset():
    if(input.text().isdigit() and int(input.text()) > 1):
        boundary_num = int(input.text())
        input.setReadOnly(True)
        btn1.setEnabled(False)
        btn2.setEnabled(True)
        input2.clear()
        input2.setReadOnly(False)
        
        global answer
        global count
        answer = random.randint(1,boundary_num)
        count = 0
    else:  
        mbox = QtWidgets.QMessageBox(Form) 
        mbox.information(Form, '錯誤', '請輸入大於1的數字')
        
def check():
    if(input2.text().isdigit()):
        global answer
        global count
        guess = int(input2.text())
        count = count + 1
        if(guess == answer):
            mbox = QtWidgets.QMessageBox(Form)       
            mbox.information(Form, '恭喜', '正確答案!你猜了'+str(count)+'次') 
            btn1.setEnabled(True)
            input.setReadOnly(False)
            input.clear()
            input2.clear()
            input2.setReadOnly(True)
            btn2.setEnabled(False)
        else:
            mbox = QtWidgets.QMessageBox(Form)   
            if(guess < answer):    
                mbox.information(Form, '錯誤答案', '更大')
            else:
                mbox.information(Form, '錯誤答案', '更小')    
    else:
        mbox = QtWidgets.QMessageBox(Form)      
        mbox.information(Form, '錯誤', '請輸入數字') 

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()    
Form.setWindowTitle('終極密碼')  
Form.resize(145, 160)              

label1 = QtWidgets.QLabel(Form)
label1.setText('輸入範圍')        
label1.move(10,10)

input = QtWidgets.QLineEdit(Form)  
input.setGeometry(90,10,30,20)     
input.setText("100")

btn1 = QtWidgets.QPushButton(Form)
btn1.setText('確認')
btn1.move(40,40)               
btn1.clicked.connect(reset)

label2 = QtWidgets.QLabel(Form) 
label2.setText('輸入答案')        
label2.move(10,90)

input2 = QtWidgets.QLineEdit(Form) 
input2.setGeometry(90,90,30,20)  

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('確認')
btn2.move(40,120)           
btn2.clicked.connect(check)

input2.setReadOnly(True)
btn2.setEnabled(False)

Form.show()                      
sys.exit(app.exec())