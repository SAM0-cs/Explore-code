#Self-Intro Script Generator
import datetime

class Person:
    def __init__(self,name,age,city,profession,hobby):
        self.name =name
        self.age = age
        self.city = city
        self.profession = profession
        self.hobby = hobby
    
    def intro(self):
        return (f"""
                Hello! My name is {self.name}. I'm {self.age} years old and live
in {self.city}. I work as a {self.profession} and I absolutely enjoy 
{self.hobby} in my free time. Nice to meet you!!""")


name=input("Enter your name:")
age=input("Enter your age:")
city=input("Enter your city:")
profession=input("Enter your Profession:")
hobby=input("Enter your hoby:") 

p1 = Person(name,age,city,profession,hobby)

intro = (p1.intro())
login = datetime.date.today().isoformat()
border = ("*"*80)

final = print(border,"\n",intro,"\n",login,"\n",border)
