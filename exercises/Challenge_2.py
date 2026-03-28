#Stylish Bio Generator For Instagram/Twittter

class Bio:
    def __init__(self,name,profession,goal,emoji,web,option):
        self.name = name
        self.profession = profession
        self.goal = goal
        self.emoji = emoji
        self.web = web
        self.option= option

    def intro(self):
        if self.option==1:
            return f"{self.emoji}\n{self.name}|{self.profession}\n☺ {self.goal}\n{self.web}😎"
        
        elif self.option == 2:
            return f"❤ {self.goal}\n{self.web}😎\n{self.emoji} {self.name}|{self.profession}"
        
        elif self.option ==3:
            return f"{self.web}✔|{self.name}😎\n{self.emoji} {self.goal}\n{self.profession}"
        else:
            return f"""option3:\n{self.web}✔|{self.name}😎\n{self.emoji} {self.goal}\n{self.profession}
\noption2:\n{self.emoji} {self.goal}\n{self.web}✔\n{self.name}😎|{self.profession}
\noption1:\n{self.name}😎|{self.profession}\n{self.emoji} {self.goal}\n{self.web}😎

 """


name = input("What is your Name:").upper()  
profession =input("What is your profssion? ").upper() 
goal = input("gave youre goal or dream in oneline? ").upper() 
emoji = input("Which is your favorite emoji ? ") 
web =input("enter your web link or handel name? ").upper() 

option =int(input("Which Option you prefer from 1,2 and 3 ?:"))  

b1 = Bio(name,profession,goal,emoji,web,option)
print("Bio")
print( "*"*90,"\n",b1.intro(),"\n","*"*90)


save = input ("Do you want to save this bio in a text file? (y/n):")
if save == "y":
    filename= f"{b1.name.lower().replace(' ','_')}_bio.txt"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(b1.intro())
    print("file is saved")



