password = input("Enter new passowrd: ")
result = {}

if len(password) >= 7:
    result["length"] = (True)
else:
    result["length"] = (False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = (uppercase)

# print(result)
if all(result):
    print("Great password there!")
elif len(result == 7):
    print("Password is not stron")
else:
    print("Your password is weak!")
