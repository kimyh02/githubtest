from tkinter import *

window=Tk()

##출력대상 ##text=문자열 ##font=글자모양 ##fg==foreground 글자 ##bg 배경색 ##anchor = 분인다 SE=SOUTH EAST
##N, NE, SE, S, SW, W, NW, CENTER
label1=Label(window, text="cookbook울")
label2=Label(window, text="열심히",font=("궁서체",30),fg="blue")
label3=Label(window, text="공부 중 입니다",bg="magenta",width=20,height=5,anchor=SE)

label1.pack() ##pack  함수를 써야만 표시된
label2.pack()
label3.pack()

window.mainloop()
