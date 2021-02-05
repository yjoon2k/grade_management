import requests 
import json
import url as url

class Student:
    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code
        self.score = []
    
    def add_score(self, score):
        self.score.append(score)



#get : 전체 학생 리스트 받아오기
#post : 새로운 학생 만들기

#d = {'Name':'최나영', 'Code':'최나영3'}
#response = requests.post(url,data = json.dumps(d), headers = headers)
#print(response.status_code)

rs2 = requests.get(url.url, headers = url.headers)

print(rs2.status_code)
init = rs2.json()

print(init[0])

st = []

for i in init:
    st.append(Student(i['Id'], i['Name'], i['Code']))

for i in st:
    if i.code[3] == '1':
        print(i.code[3])
    elif i.code[3] == '2':
        print(i.code[3])
    elif i.code[3] == '3':
        print(i.code[3])





#url/name/code - get: 이름/코드의 학생 불러오기
#url/id - get: id의 학생 불러오기
