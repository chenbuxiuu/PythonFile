from student import *
from types import MethodType

bart = Student('Bart Simpson', 59)

#bart.age=12
bart.print_score()

def setScore(self,score):
    self.score=score

Student.setScore=setScore

bart.setScore(60)
bart.print_score()
