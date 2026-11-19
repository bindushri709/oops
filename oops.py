class student:
    name="ram"
s1=student()
s1.name="Ram"
print(s1.name)
class student:
    name="ram"
    age="20"
s1=student()
s2=student()
print(s1.age)
print(student.name)
print(s2.name)
class college:
    name="gcem"
    loc="hoodi"

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print(self.name, self.age, self.dept)
    def change_name(self,new):
        self.name=new

s1 = college("Raju", 20, "ise")
s2=college("ramu",21,"ECE")
print("Before")
s2.display()
s2.change_name("ram")
print("after")
s2.display()
print('-----------------')
s2.display()
print('-----------------')
college.change_name(s1,"Raj")
college.display(s1)
print(s1.name)
class college:
    name="gcem"
    loc="hoodi"

    @classmethod
    def disp(cls):
        print(cls.name, cls.loc)

    @classmethod
    def change_loc(cls, new):
        cls.loc = new

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print(self.name, self.age, self.dept)

    def change_name(self, new):
        self.name = new

s1 = college("Raju", 20, "ise")
s2=college("ramu",21,"ECE")
print("Before")
s2.display()
s2.change_name("ram")
print("after")
s2.display()
print('-----------------')
college.change_name(s1,"Raj")
college.display(s1)
print('-----------------')
s1.disp()
s2.disp()
college.change_loc("E_city")
college.disp()
print(s1.loc)







