import math, functools


def calculate_total_fuel_requirement(arr_input):
    #We use reduce() to add all the calculated fuel values in our input WITHOUT adding its value to the module
    return functools.reduce(lambda a,b: a+b, [calculate_suplementary_fuel(fuel) - fuel for fuel in arr_input])

def calculate_suplementary_fuel(input):
    current = math.floor(input/3)-2

    if current <= 0:
        return input
    else:
        return input + calculate_suplementary_fuel(current)