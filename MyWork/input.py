from tkinter import *

def process():
    print(f"이름={A[0].get()}, 직업={A[1].get()}, 나이={A[2].get()}")

def reset():
    for x in range(3):
        A[x].delete(0, END)

window = Tk()
Label(window, text="이름", padx=5).grid(row=0, column=0)
Label(window, text="직업", padx=5).grid(row=1, column=0)
Label(window, text="나이", padx=5).grid(row=2, column=0)

A = []
for x in range(3):
    A.append(Entry(window))
    A[x].grid(row=x, column=1)
    
f = Frame(window)
f.grid(row=3, column=1)

b1 = Button(f, text="처리", command=process).pack(side=LEFT)
b2 = Button(f, text="다시 입력", command=reset).pack(side=LEFT)

window.mainloop()