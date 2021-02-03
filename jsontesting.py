import json

url = "https://minshigeestudentmanagerapi.herokuapp.com/api/students/"

with open(url + "홍길동/아주대19") as json_file:
    json_Data = json.load(json_file)

