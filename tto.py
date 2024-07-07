from tkinter import *

# i번째 버튼을 누를 수 있는지 검사한다. 누를 수 있으면 X나 O를 표시한다. 
def checked(i):
    global player
    button = list[i]	# 리스트에서 I번째 버튼 객체를 가져온다. 

	  # 버튼이 초기상태가 아니면 이미 누른 버튼이므로 아무것도 하지 않고 리턴한다.
    if   button["text"] != "            ":
        return
    button["text"] = "     " + player+"      "
    button["bg"] = "yellow"
    old_player = player
    if   player=="X":
        player = "O"
        button["bg"] = "yellow"
    else :
        player = "X"
        button["bg"] = "lightgreen"
    
    checkFinish(i, old_player)
    
def checkFinish(pos, player):
    cmsg = list[pos]["text"]
    row = pos // 3
    col = pos % 3
    for c in range(3):
        if list[row*3 + c]["text"] != cmsg:
            break
    else:
        finished(player)
        
    # for r in range(3):
    #     if list[r*3 + col]["text"] != cmsg:
    #         break
    # else:
    #     finished(player)
    # if row == col:
    #     for x in range(3):
    #         if list[x*3 + x]["text"] != cmsg:
    #             return
    
def finished(winner):
    label["text"] = f"게임 종료! 승자 = {winner}"
    for i in range(9):
        list[i]["state"] = DISABLED

window = Tk()		# 윈도우를 생성한다.  
player="X"		# 시작은 플레이어 X이다. 
list = []

# 9개의 버튼을 생성하여 격자 형태로 윈도우에 배치한다. 
for i in range(9):
    b = Button(window, text="            ", command=lambda k=i: checked(k))
    b.grid(row=i//3, column=i%3)
    list.append(b)	# 버튼 객체를 리스트에 저장한다. 

label = Label(window, fg="red")
label.grid(row=3, column=0, columnspan=3)
window.mainloop()
