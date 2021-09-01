def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def length_of_string(x):
    return len(x)

def join_string(x,y):
    return x + y

def add_string_as_number(x, y):
    return int(x) + int(y)

def number_to_full_month_name(x):
    calender = ("January", "February", "March","April","May","June","July","August","September","October","November","December")
    return (calender[x - 1])
print(number_to_full_month_name(1))

def number_to_short_month_name(x):
    calender = ("Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
    return (calender[x -1])

def volume_of_cube(x):
    return x**3

print(volume_of_cube(3))

def reverse_string(x):
    return x[::-1]

def fahrenheit_to_celsius(x):
    return ((x-32)*(5/9))
