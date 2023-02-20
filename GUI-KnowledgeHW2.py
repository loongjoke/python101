from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk() #หน้าจอหลัก
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย') #ชื่อโปรแกรม
GUI.geometry('500x600') #ขนาดโปรแกรม


L1 = Label(GUI,text='โปรแกรมบันทึกค่าใช้จ่าย',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

######
def Button2():
    text = 'เงินเดือน 20000'
    messagebox.showinfo('รายรับ ',text)


FB1 = LabelFrame(GUI,text='January') #คล้ายกระดาน
FB1.place(x=80,y=100)
B2 = ttk.Button(FB1,text='มกราคม',command=Button2)
B2.pack(ipadx=10,ipady=10)
######
def Button3():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)


FB1 = LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=80,y=180)
B3 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button3)
B3.pack(ipadx=20,ipady=20)
######
def Button4():
    text = 'Phthon 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่10-20 ก.พ.',text)


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=80,y=270)
B4 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button4)
B4.pack(ipadx=20,ipady=20)
######

GUI.mainloop()
