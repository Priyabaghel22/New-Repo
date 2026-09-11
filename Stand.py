import random 

user1 = "Priya"
user1  = input("enter the number")

if 1<= user1 <= 10:
    print("valid number")
else:
    print("invalid number")


user2 = "Riya"
user2 = input("enter the number")   

if 1<= user2 <= 10:
    print("valid number")
else:
    print("invalid number")

random_number = random.randint(1,10)
print("Random number:", random_number)

answer1 = user1*random_number
answer2 = user2*random_number

print("user1's answer:", answer1)
print("user2's answer:", answer2)

if answer1 == random_number:
    print("user1 is correct!")
else:
    print("user1 is incorrect.")