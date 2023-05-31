try: 
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    decimal_value = value/total_value
    percentage = decimal_value * 100

    formatted_percentage = percentage
    print(f"{formatted_percentage}%")
    
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("YOR TOTAL VALUE CANNOT BE ZERO.")
