import pickle
from tkinter import *

def save():
    file = open("user.dat", "ab")
    user = {}
    user[forms[0].get()] = (forms[1].get(), forms[2].get())
    pickle.dump(user, file)
    file.close()
    reset()

def reset():
    for x in range(3):
        forms[x].delete(0, END)
    forms[0].focus_set()

def load():
    file = open("user.dat", "rb")
    uinfo = []
    try:
        while True:
            uinfo.append(pickle.load(file))
    except EOFError:
        file.close()
    print(uinfo)

window = Tk()
Label(window, text="이름", padx=10).grid(row=0, column=0)
Label(window, text="직업", padx=10).grid(row=1, column=0)
Label(window, text="나이", padx=10).grid(row=2, column=0)

forms = []
for x in range(3):
    forms.append(Entry(window))
    forms[x].grid(row=x, column=1)
    
f = Frame(window)
f.grid(row=3, column=0, columnspan=2, sticky=E+W)
Button(f, text="파일에 저장", command=save).pack(side=LEFT)
Button(f, text="다시 입력", command=reset).pack(side=LEFT)
Button(f, text="파일 내용 출력", command=load).pack(side=LEFT)

window.mainloop()