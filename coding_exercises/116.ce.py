def get_max():
    grades = [9.6, 9.2, 9.7]
    minimum = min(grades)
    maximum = max(grades)
    
    message = f"Max: {maximum}, Min: {minimum}"
    return message
    


max_grades = get_max()
print(max_grades)

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return(maximum)
    
celsius = get_maximum()
 
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)