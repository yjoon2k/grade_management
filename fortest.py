import requests 
import json
from tkinter import *
from functools import partial
import matplotlib.pyplot as plt
import numpy as np
import myurl as url
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

st_1 = []
st_2 = []
st_3 = []

class Student:
    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code
        self.score = []
    
    def add_score(self, score):
        self.score.append(score)


def grade_pick_1():
    frame_student_2.pack_forget()
    frame_student_3.pack_forget()
    frame_student_1.pack(side="right")

def grade_pick_2():
    frame_student_1.pack_forget()
    frame_student_3.pack_forget()
    frame_student_2.pack(side="right")

def grade_pick_3():
    frame_student_2.pack_forget()
    frame_student_1.pack_forget()
    frame_student_3.pack(side="right")

def printscore(i):
    x = np.arange(len(i.score))
    cnt = []
    for j in range(1, len(i.score) + 1):
        cnt.append(j)
    
    plt.bar(x, i.score)
    plt.xticks(x, cnt)
    plt.title(i.name+"학생의 성적그래프")
    plt.show()

def init():
    rs_init = requests.get(url.url, headers = url.headers)
    print(rs_init.status_code)
    init = rs_init.json()
    for i in init:
        if i['Code'][3] == '1':
            st_1.append(Student(i['Id'], i['Name'], i['Code']))
        elif i['Code'][3] == '2':
            st_2.append(Student(i['Id'], i['Name'], i['Code']))
        elif i['Code'][3] == '3':
            st_3.append(Student(i['Id'], i['Name'], i['Code']))

init()

    

root = Tk()
root.title("성적관리프로그램")
root.geometry("540x380+200+100")

frame_grade = LabelFrame(root, relief = "solid", bd = 1)
frame_grade.pack(side="left")
Button(frame_grade, text = "1학년", command = grade_pick_1).pack()
Button(frame_grade, text = "2학년", command = grade_pick_2).pack()
Button(frame_grade, text = "3학년", command = grade_pick_3).pack()

top_label = Label(root, text="성적관리프로그램")
top_label.pack(side="top")

frame_student_1 = LabelFrame(root, text = "1학년")
frame_student_2 = LabelFrame(root, text = "2학년")
frame_student_1.pack(side="right")
frame_edit = Frame(root, relief = "solid", bd = 1)
frame_edit.pack(side = "bottom")
Button(frame_edit, text = "추가").grid(row = 0, column = 0)
Button(frame_edit, text = "수정").grid(row = 0, column = 1)
Button(frame_edit, text = "삭제").grid(row = 0, column = 2)
frame_student_3 = LabelFrame(root, text = "3학년")
for i in st_3:
    print(i.name)
    Button(frame_student_3, text = i.name, command = partial(printscore,i)).pack()
root.mainloop()