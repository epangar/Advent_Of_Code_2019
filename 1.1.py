import math, functools

def calculate_total_requirement(arr_input):
    #We use reduce() to add all the calculated fuel values in our input
    return functools.reduce(lambda a,b: a+b, [calculate_fuel(fuel) for fuel in arr_input])

def calculate_fuel(input):
    return (math.floor(input/3)-2)
        

