#Definition of a Class
class student():
    def __init__(self,name,age,year,city): #constructor initialisation
        print("hello")
        self.name=name
        self.age=age
        self.year=year
        self.city=city
    def info(self):
        self.name=input("Enter your name?")
        self.age=input("Enter your age?")
        self.year=input("Enter your year?")
        self.city=input("Enter your city?")
    def out(self):
        print(self.name)
        print(self.age)
        print(self.year)
        print(self.city)
s1=student("Nya",16,11,"New York")
s2=student("Leah",15,10,"Las Vegas")
s1.out()
s1.info()
s1.out()
s2.out()
s2.info()
s2.out()