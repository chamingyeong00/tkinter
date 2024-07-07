from tkinter import *
import random

def run():
    label["text"] = random.randint(1, 6)
    
window = Tk()
window.geometry("300x300")
window.title("주사위 던지기")

label = Label(window, text=1, fg="red", font=("Arial", 100, "bold"))
label.pack(side=LEFT, padx=50)
button = Button(window, text="굴리기", fg="blue", font = ("Arial", 20, "bold"), command=run)
button.pack(side=RIGHT)

window.mainloop()