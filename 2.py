from tkinter import *
import pickle
def save():
    file = open("user.dat", "ab")
    pickle.dump({forms[0].get(): (forms[1].get(), forms[2].get())}, file)
    file.close()    

def output():
    A = []
    file = open("user.dat", "rb")
    try:
        while True:
            A.append(pickle.load(file))
    except EOFError:
        pass
    file.close()
    print(A)

def reset():
    for x in range(3):
        forms[x].delete(0, END)
    forms[0].focus_set()

window = Tk()
window.title("데이터 입력")
labels = ["이름", "직업", "나이"]
forms = []


for x in range(3):
    Label(window, text=labels[x], font=("Arial", 14)).grid(row=x, column=0)
    entry = Entry(window,font=("Arial", 14), fg="blue")
    entry.grid(row=x, column=1 )
    forms.append(entry)

frame = Frame(window)
frame.grid(row=3, column=1)
Button(frame, text="파일에 저장", font=("Arial", 14), command=save).pack(side = LEFT)
Button(frame, text="다시 입력", font=("Arial", 14), command=reset).pack(side = LEFT)
Button(frame, text="파일 내용 출력", font=("Arial", 14), command=output).pack(side = LEFT)

window.mainloop()