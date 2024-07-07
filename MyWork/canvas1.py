from tkinter import *

def up():
    x1, y1, x2, y2 = canvas.coords(rect)
    canvas.coords(rect, x1-5, y1-5, x2+5, y2+5)

def down():
    x1, y1, x2, y2 = canvas.coords(rect)
    canvas.coords(rect, x1+5, y1+5, x2-5, y2-5)
    
def callback(event):
    canvas.focus_set()
    if event.keysym == 'Up':
        canvas.move(rect, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(rect, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(rect, -5, 0)
    elif event.keysym == 'Right':
        canvas.move(rect, 5, 0)

window = Tk()
window.title("사각형 크기 변경하기")
canvas = Canvas(window, width=600, height=600)
canvas.pack()

rect = canvas.create_rectangle(250, 250, 350, 350, fill="red")

f = Frame(window)
f.pack()
Button(f, text="size up", font="Helvetica 20 bold", command=up).pack(side=LEFT, padx=50)
Button(f, text="size down", font="Helvetica 20 bold", command=down).pack(side=LEFT, padx=50)

window.bind("<Key>", callback)
window.mainloop()