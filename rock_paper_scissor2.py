##
#	이 프로그램은 가위, 바위, 보 게임을 구현한다. 
#
import random
from tkinter import *

window = Tk()
Label(window, text="선택하세요", font=("Helvetica", "16")).pack()
frame = Frame(window)

rock_image = PhotoImage(file="rock.png")
paper_image = PhotoImage(file="paper.png")
scissors_image = PhotoImage(file="scissors.png")

# 교재 오타!!
def pass_s():
    user_image["image"] = scissors_image
    decide("가위")
def pass_r():
    user_image["image"] = rock_image
    decide("바위")
def pass_p():
    user_image["image"] = paper_image
    decide("보")

rock = Button(frame, image=rock_image, command=pass_r)
rock.pack(side="left")
paper = Button(frame, image=paper_image, command=pass_p)
paper.pack(side="left")
scissors = Button(frame, image=scissors_image, command=pass_s)
scissors.pack(side="left")

frame.pack()

frame2 = Frame(window)
user_image = Label(frame2)
computer_image = Label(frame2)
user_image.pack(side=LEFT)
computer_image.pack(side=LEFT)
frame2.pack()

output = Label(window, text="", font=("Helvetica", "16"))
output.pack()

def decide(human):
    computer = random.choice(["가위", "바위", "보"])
    if   computer == "바위":
        computer_image["image"] = rock_image
    elif   computer == "보":
        computer_image["image"] = paper_image
    else:
        computer_image["image"] = scissors_image

    if   (computer == "바위" and human == "보") or (computer == "보" and human == "가위")\
            or (computer == "가위" and human == "바위"):
        result = "인간 승리!"
    elif   computer == human:
        result = "비겼습니다."
    else:
        result = "컴퓨터 승리!"
    output.config(text="인간: " + human + "   컴퓨터:" + computer + "    " + result)


window.mainloop()
