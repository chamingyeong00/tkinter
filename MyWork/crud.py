import pymysql
from tkinter import *
from tkinter import messagebox

def retrieve():
    try:
        sql = "select * from student where sid = %s"
        val = (form[0].get(), )
        mc.execute(sql, val)
        result = mc.fetchone()
        if result == None:
            raise TypeError("조건을 만족하는 학생이 없습니다.")
        reset()
        for col in range(len(labels)):
            form[col].insert(0, result[col])
    except TypeError as e:
        messagebox.showerror("오류", "오류가 발생하였습니다: " + str(e))

def insert():
    try:
        val = []
        for col in range(len(labels)):
            val.append(form[col].get())
        sql = "insert into student values (%s, %s, %s, %s, %s, %s, %s, %s)"
        mc.execute(sql, val)
        mydb.commit()
        if mc.rowcount == 1:
            messagebox.showinfo("성공", "1개의 레코드가 정상적으로 추가되었습니다.")
    except TypeError as e:
        messagebox.showerror("오류", "오류가 발생하였습니다: " + str(e))

def update():
    try:
        val = []
        for col in range(1, len(labels)):
            val.append(form[col].get())
        val.append(form[0].get())
        sql = "update student set sname = %s, deptno = %s, advisor = %s, gen = %s, " + \
                "addr = %s, birthdate = %s, grade = %s where sid = %s"
        mc.execute(sql, val)
        mydb.commit()
        if mc.rowcount == 1:
            messagebox.showinfo("성공", "레코드가 정상적으로 수정되었습니다.")
    except TypeError as e:
        messagebox.showerror("오류", "오류가 발생하였습니다: " + str(e))

def delete():
    try:
        val = (form[0].get(), )
        sql = "delete from student where sid = %s"
        mc.execute(sql, val)
        mydb.commit()
        if mc.rowcount == 1:
            messagebox.showinfo("성공", "정상적으로 레코드가 삭제되었습니다.")
            reset()
    except TypeError as e:
        messagebox.showerror("오류", "오류가 발생하였습니다: " + str(e))

def reset():
    for x in range(len(labels)):
        form[x].delete(0, END)
    form[0].focus_set()

window = Tk()
window.title("Student 테이블")
window.geometry('600x350')

mydb = pymysql.connect(host="localhost", user="root", password="1234", db="StudentDB")
mc = mydb.cursor()

labels = ['학번', '이름', '학과', '지도교수', '성별', '주소', '생일', '학점']
form = []
for i in range(len(labels)):
    Label(window, text=labels[i], font=('Hevetica', 16, 'bold')).grid(row=i, column=0)
    form.append(Entry(window, fg='blue', width=30, font=('Helvetica', 20, 'bold')))
    form[i].grid(row=i, column=1)

f = Frame(window)
f.grid(row=len(labels), pady=10, column=1)
Button(f, text="검색", padx=10, font=('Hevetica', 16, 'bold'), command=retrieve).pack(side=LEFT)
Button(f, text="추가", padx=10, font=('Hevetica', 16, 'bold'), command=insert).pack(side=LEFT)
Button(f, text="수정", padx=10, font=('Hevetica', 16, 'bold'), command=update).pack(side=LEFT)
Button(f, text="삭제", padx=10, font=('Hevetica', 16, 'bold'), command=delete).pack(side=LEFT)
Button(f, text="다시 입력", font=('Hevetica', 16, 'bold'), command=reset).pack(side=LEFT)

window.mainloop()