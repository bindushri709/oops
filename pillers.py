'''class A:          #single inheritence
    a=10
class B(A):
    b=20
ob1=B()
print(ob1.a,ob1.b)
class Bank:
    bname = 'SBI'
    bloc = 'DDS'

    def __init__(self, name, phno, eid):    #example prgm for single inheritence
        self.name = name
        self.phno = phno
        self.eid = eid

    def display(self):
        print(self.name, self.phno, self.eid)


c1 = Bank("bindu", 8217052525, 'bindu@gmail.com')
c1.display()


class Bank_details(Bank):
    founder = 'ABC'

    def __init__(self, name, phno, eid, add, pan):
        super().__init__(name, phno, eid)
        self.add = add
        self.pan = pan

    def display(self):
        print(self.name, self.phno, self.eid, self.add, self.pan)


c1 = Bank_details("bindu", 8217052525, 'bindu@gmail.com', 'dds', 'dsknsdshi')
c1.display()

class A:                             #multilevel inheritence
    a=10
class B(A):
    b=20
class C(B):
    c=30
class D(C):
    d=40
ob1=D()
print(ob1.a,ob1.b,ob1.c,ob1.d)

class school:         #ex for multilevel inheritence
    sname='GHPS'
    sloc='DDS'
    
class college(school):
    cname='GPN'
    cloc='hoodi'
    
class university(college):
    uname='Dayanand'
    uloc='banglore'

    @classmethod
    def display(cls):
        print(cls.sname,cls.sloc,cls.cname,cls.cloc,cls.uname,cls.uloc)   
university.display()

class school:          #multiple inheritence
    sname='GHPS'
    sloc='DDS'
    
class college():
    cname='GPN'
    cloc='hoodi'
    
class university(college,school):
    uname='Dayanand'
    uloc='banglore'

    @classmethod
    def display(cls):
        print(cls.sname,cls.sloc,cls.cname,cls.cloc,cls.uname,cls.uloc)   
university.display()
print(university.mro())

     
class school:          #multiple inheritence
    sname='GHPS'
    sloc='DDS'
    
class college(school):      #heirarchical inheritence
    cname='GPN'
    cloc='hoodi'
s1=college()
print(s1.sname,s1.sloc,s1.cname,s1.cloc)
class university(school):
    uname='Dayanand'
    uloc='banglore'
s2=university()
print(s2.sname,s2.sloc,s2.uname,s2.uloc)

class vehicle:
    type='ABC'   #ex for heirarchital
    brand='XYZ'
class TVS(vehicle):
    type='2 weeler'
    brand='TVS'
s1=TVS()
class CAR(vehicle):
    type='4 weeler'
    brand='TATA'
s2=CAR()
print(s1.type,s1.brand)
print(s2.type,s2.brand)

class Bank:
    bname = 'SBI'
    bloc = 'DDS'                                 #hybrid inheritence

    def __init__(self, name, phno, eid):
        self.name = name
        self.phno = phno
        self.eid = eid

    def display(self):
        print(self.name, self.phno, self.eid)


class Bank_details(Bank):
    founder = 'ABC'

    def __init__(self, name, phno, eid, add, pan):
        super().__init__(name, phno, eid)
        self.add = add
        self.pan = pan

    def display(self):
        print(self.name, self.phno, self.eid, self.add, self.pan)


class Loan:
    def __init__(self, loan_type):
        self.loan_type = loan_type

    def show_loan(self):
        print("Loan Type:", self.loan_type)


class Customer(Bank_details, Loan):
    def __init__(self, name, phno, eid, add, pan, loan_type):
        Bank_details.__init__(self, name, phno, eid, add, pan)
        Loan.__init__(self, loan_type)

    def display_details(self):
        print("Bank Name:", self.bname)
        print("Name:", self.name)
        print("Phone:", self.phno)
        print("Email:", self.eid)
        print("Address:", self.add)
        print("PAN:", self.pan)
        self.show_loan()


c1 = Customer("Bindu", 8217052525, "bindu@gmail.com",
              "DDS", "ABCDE1234F", "Home Loan")

c1.display_details()

class demo:                                    #method overloading
    @staticmethod
    def sam():
        print("Why are you coming late")
    a=sam()
    @staticmethod
    def sam(a,b):
        print(a+b)
    b=sam
    @staticmethod
    def sam(a,b,c):
        print(a*b*c)
    c=sam
ob=demo()
ob.a
ob.b(10,20)
ob.c(1,2,3)

class demo:                             #operator overloading
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return demo(self.value+other.value)
a=demo(100)
b=demo(200)

c=a+b
print(c.value) 
print(type(c.value))  

print("-------concatenation-----------")
s=demo("Hi ")
s1=demo("Good morning")     
result=s+s1
print(result.value)
print(type(result.value))
        
class Bank:
    __deposit=100000
    def __init__(self,name,phone,accno):
        self.name=name
        self.phone=phone
        self.__accno=accno
b=Bank("bindu",2898559898,1546464)
print(b.name)
print("syntax1 for accessing private value")
print(b._Bank__accno)
print(b._Bank__deposit)     #syntax1 for accessing member inside the class(obj._classname__var/method)
print(Bank._Bank__deposit)  #syntax2 for accessing member inside the class(classname._classname__var/method)
Bank._Bank__deposit=10000
print(b._Bank__deposit)    #syntax for changing values for variable in private
print(Bank._Bank__deposit)

class bank:
    def __init__(self,name,bal):
        self.name=name
        self.__bal=bal
    def get_bal(self):
        return self.__bal
    def set_bal(self,amount):
        self.__bal=amount
    
    ##deposit
    
    def deposit(self,amount):
        self.set_bal(self.get_bal() + amount)
        
    ##withdraw
    
    def withdraw(self,amount):
        if amount<=self.get_bal():
            self.set_bal(self.get_bal()-amount)
            print("withdrwan successful", amount)
        else:
            print("Insufficient balence")
b=bank("bindu",1000)
print("------before------")
print(b.get_bal())
print("------after-------")

b.deposit(500)
print(b.get_bal())

print("------after withdrwan--------")
b.withdraw(200)
print(b.get_bal())'''

from abc import ABC,abstractmethod

class student(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod   # this is only showing us
    def study(self):
        pass
    @abstractmethod
    def write(self):
        pass
    
class school(student):  #child class will run in backend
    def study(self):
        print(self.name,"studying")
        
    def write(self):
        print(self.name,"writing")
        
s1=school("Raj")
s2=school("komal")
s1.study()
s2.write()
        
        
        