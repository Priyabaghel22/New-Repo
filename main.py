people_list=[]
class person:
 def _init_(self,name,age,address,course,city):
    self.name = name
    self.age = age
    self.address = address
    self.course = course
    self.city = city 

    for i in range(5):
        name = input("enter your name: ")
        age = int(input("enter your age: "))
        address = input("enter your address: ")
        course = input("enter your course: ")
        city = input("enter your city:")

        person =person(name, age, address, course,city)
        person.append(person)



    