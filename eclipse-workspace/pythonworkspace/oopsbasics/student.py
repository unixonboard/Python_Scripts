from bleach._vendor.html5lib._ihatexml import name
class Student:
    major = "CSE"

    def __init__(self,rollnum,name):
        self.rollnu = rollnum
        self.name = name
        
s1=Student(1,"John")
s2=Student(2,"Bill")
print(s1.major)
print(s2.major)
print(s1.rollnu)
print(s2.rollnu)
print(s1.name)
print(s2.name)
print(Student.major)