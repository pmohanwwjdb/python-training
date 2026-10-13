# import json
# employee = {"name":"dave","age":25,"position":"webdav"}
# filepath =  "output.json"
# with open (filepath,"w") as file:
#     json.dump(employee,file)

#CSV

# import csv
# employee = [["Name","Age"],["dave",25],["tony",68],["gray",90],["jinwoo",44],["don",333]]
# filepath = "output.csv"
# with open (filepath,"w") as file:

#     write = csv.writer(file)
#     for data in employee:
#         write.writerow(data)


#oop(object oriented programming)

#topics
# object:- a bundle of related attributes and methods representing a real worl entity

# class Car:
#     def __init__(self, model, year, colour, for_sale):
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.for_sale = for_sale
#     def drive(self):
#         print(f"you are driving{self.model}")
#     def stop(self):
#         print(f"you are stoping{self.model}")
#     def describe(self):
#         print(f"your car is {self.model}{self.year} the colour is {self.colour}. Is it for sale{self.for_sale}")





# car1 = Car("Lamborghini", 1999, "Black", False)
# car2 = Car("mustang",2006,"Red",True)
# # car1.drive()
# car2.stop()
# car1.describe()


# class Student:
#     def __init__(self, name, rollno, age):
#         self.name = name 
#         self.rollno = rollno
#         self.age = age 
#     def read(self):
#         print(f" {self.name} is reading")
#     def play(self):
#         print(f"the roll no {self.rollno} is playing")
#     def data(self):
#         print(f"name :-{self.name} age :- {self.age}  rollno:-{self.rollno}")
                


# student1= Student("ronaldo",7,49)
# student2 = Student("haland",222,33)
# student3 = Student("naymer",111,21)
# student4 = Student("messi", 999,100)
# student5 = Student("chetri",2323,30)

# student1.read()
# student1.play()
# student1.data()

