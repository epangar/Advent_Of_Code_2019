def intcode(arr_input):
    for i in range(0, len(arr_input), 4):
        #Check the operation, the second and third parameters and their future position
        current_code =  arr_input[i]
        second = arr_input[i+1]
        third = arr_input[i+2]
        place = arr_input[i+3]
        
        if current_code == 99:
            break
        elif current_code == 1:
            arr_input[place] = arr_input[second] + arr_input[third]
        elif current_code == 2:
            arr_input[place] = arr_input[second] * arr_input[third]
    
    return arr_input