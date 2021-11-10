import math, functools

def calculate_total_fuel_requirement(arr_input):
    answer = functools.reduce(lambda a,b: a+b, [calculate_fuel(fuel) for fuel in arr_input])
    return answer

def calculate_fuel(input):
    return (math.floor(input/3)-2)
        

