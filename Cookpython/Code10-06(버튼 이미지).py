from tkinter import *
from tkinter import messagebox

##함수 선언 부분##
def myFunc() :
    messagebox.showinfo("원피스 버튼","내 동료 할래^^?")

##메인 코드 부분##
window=Tk()
photo=PhotoImage(file="gif/onepiece.gif")
button1=Button(window,image=photo, command=myFunc)

button1.pack()

window.mainloop()
