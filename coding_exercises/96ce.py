password = input("Enter a new pasword:")

if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Password is OK, but not too strongl")
else:
    print("Your password is weak.")
