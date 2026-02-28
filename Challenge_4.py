# Minutes Alive Calculator

class Life:
    def __init__(self,age):
        self.age=age
    
    def calculate(self,age):
            return f"""\n Youre Aproximately! :
            - {age*365.25} days old,
            - {age*365.25*24} hours old,
            - {age*365.25*24*60} minutes old"""
        
    def floatValue(self,age):
        while True:
            try:
                return float(input(age))
                
            except:
                print("Enter valid input or number!!")
               


age = 0
l1 = Life(age)
age = l1.floatValue("Enter your age in years? ")
print(l1.calculate(age))

again = "y"
while again =="y":
    again =input("Would you like to try again?(y/n)").strip().lower()
    if again=="y":
        age = l1.floatValue("Enter your age in years? ")
        print(l1.calculate(age))
    else:
        print("\nGood Bye!!")