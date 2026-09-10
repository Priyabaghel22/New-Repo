import random 

user1  = "Priya"

user1 = int(input("enter a number between 1 and 10:"))

if 1<=user1<=10:
    print("Valid input!")
else:
    print("Invalid input!")

user2 = "Riya"
user2 = int(input("enter a number between 1 and 10:"))

if 1<=user2<=10:
    print("Valid input!")
else:
    print("Invalid input!")


random_number=random.randint(1,10)
print("random number is:", random_number)

answer1 = user1*random_number
answer2 = user2 *random_number

print("priya answer is ",answer1)
print("riya answer is ",answer2)

if answer1 == answer2:
    print("pass")
else:
    print("fail")
    