from tkinter import *
import math

def leftClickButton(evet):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if BMI < 18.5:
        labelResult.configure(text="ผอมเกินไป")
    elif BMI < 23:
        labelResult.configure(text="น้ำหนักปกติ")    
    elif BMI < 25:
        labelResult.configure(text="น้ำหนักเกิน")    
    elif BMI < 30:
        labelResult.configure(text="อ้วน")
    else:
        labelResult.configure(text="อ้วนมาก")    
       
MainWindow = Tk()
lableHeight = Label(MainWindow, text = "ส่วนสูง (cm)").grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
lableWeight = Label(MainWindow, text = "น้ำหนัก (kg)").grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.bind("<Button-1>", leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()
