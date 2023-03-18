#Day1
# user_prompt = "Enter a todo:"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3, "Hello"]
# print(todos)
# print(type(todo1))

# Day2
# user_prompt = "Enter a todo:"

# while 2 > 1:
#     todo = input(user_prompt)

# while True:
#     todo = input(user_prompt)
#     print(todo)
#     print("Next...")

# todos = []
# while True:
#     todo = input(user_prompt)
#     todos.append(todo)
#     print(todos)
 
# while True:
#     print("Hello")
# Coding Exercises 1.1
# name = input("Enter you first name:")
# print(name.capitalize())

# Coding Exercises 1.2
# name = input("What is your name? ")
# while True:
#     capitalized_name = name.capitalize()
#     print(capitalized_name)

# #Coding Exercise 1.3

# while True:
#     name = input("What is your name? ")
#     print(name.capitalize())

# while True:
#     print("Hello")

# greeting = "hello"
# print(greeting.upper())

# countries = []
 
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)

# ids = ["XF345_89", "XER76849", "XA454_55"]
 
# x = 0
 
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

length = float(int(input("Enter length: ")))
width = float(int(input("Enter width: ")))
 
perimeter = (length + width) * 2
area = length * width
 
print("Perimeter is", perimeter)
print("Area is", area)
 
if perimeter < 14 and area > 10:
    print("OK")
else:
    print("NOT OK")
