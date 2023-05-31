try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter a rectangle length: "))
    if width == length:
        print("Width and length have to be different numbers to create a length")
    else:
        area = width * length
        print(area)
except ValueError:
    print("Please enter a number.")