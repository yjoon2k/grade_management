class Student:
    score = []
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def add_grade(self, grade):
        self.score.append(grade)
        