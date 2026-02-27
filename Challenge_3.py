#Simple Bill Splitter

def get_float(prompt):
    while True:

        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a Valid number.")

num_person = 0
num_pepole = get_float("How many pepoles are there in  a group?:")
num_person += int(num_pepole)
names = []

for i in range(num_person):
    name = input(f"Enter name of person_{i+1}:") 
    names.append(name)

total_bill = get_float("Enter the bill amount in number only: ")
share = round(total_bill/num_pepole)

print("\n"+"*"*40+"\n")
print(f"The total bill is : {total_bill}")
print(f"Each person Owes {share} rupees")

for name in names:
    print(f"{name} owes {share} rupees")

print("\n"+"*"*40 +"\n")
