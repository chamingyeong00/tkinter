from tkinter import *

window = Tk()
counter = 0

def clicked():
    global counter
    counter += 1
    label['text'] = '버튼 클릭 횟수: ' + str(counter)
        
label = Label(window, text="아직 눌려지지 않음")
label.pack()

button = Button(window, text="증가", command=clicked)
button.pack()

def reset():
    global counter
    counter =0
    label['text'] = '버튼 클릭 횟수: ' + str(counter)

button = Button(window, text="리셋", command=reset)
button.pack()

window.mainloop()