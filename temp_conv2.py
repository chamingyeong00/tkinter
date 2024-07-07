##
#	온도 변환 프로그램을 GUI 기반으로 구현한다. 
#
from tkinter import *

# 이벤트 처리 함수를 정의한다. 
def ftoc():
    tf = float(e1.get())		# e1에서 문자열을 읽어서 부동소수점형으로 변경
    tc = (tf-32.0)*5.0/9.0		# 화씨 온도를 섭씨 온도로 변환한다. 
    e2.delete(0, END)			# 처음부터 끝까지 지운다.
    e2.insert(0, str(round(tc, 2)))		# tc 변수의 값을 문자열로 변환하여 추가한다.
    
def ctof():
    tc = float(e2.get())		# e1에서 문자열을 읽어서 부동소수점형으로 변경
    tf = tc*1.8+32		# 화씨 온도를 섭씨 온도로 변환한다. 
    e1.delete(0, END)			# 처음부터 끝까지 지운다.
    e1.insert(0, str(round(tf, 2)))		# tc 변수의 값을 문자열로 변환하여 추가한다.
    
def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    e1.focus_set()

window  = Tk()

Label(window , text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text="화씨->섭씨", command=ftoc).grid(row=2, column=1, sticky=W+E)
Button(window, text="섭씨->화씨", command=ctof).grid(row=2, column=0, sticky=W+E)
Button(window, text="Reset", command=reset).grid(row=3, column=0, columnspan=2, sticky=W+E)
window.mainloop()