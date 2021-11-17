import math

def distance(first, second):
    
    start = [0,0]
    
    final_first = move_through_matrix(first, start)
    
    final_second = move_through_matrix(second, start)
    


    #Equal_points   
    equal_points = []
    for k in range(1, len(final_first)):
        point = final_first[k]
            
        if point in final_second:
            equal_points.append(point)
    
    equal_points.sort(key = lambda arr: arr[0]+arr[1])

    shortest = equal_points[0]

    return shortest[0]+shortest[1]

def sum_two_arrays(arr1, arr2):
    
    answer = []
    LEN1 = len(arr1) 
    LEN2 = len(arr2)
    if LEN1 == LEN2:
        for i in range(0,LEN1):
            current1 = arr1[i]
            current2 = arr2[i]

            answer.append(current1 + current2) 
    
    return answer



def move_through_matrix(arr_steps, point_to_move):
    #[Horizontal, vertical]
    direction = {
        'R': [1,0],
        'U': [0,1],
        'D': [0,-1],
        'L': [-1,0]
    }

    points_it_has_passed = [point_to_move.copy()]
    
    for instruction in arr_steps:
        #The direction to follow (Up, Down, Left or Right)
        current_direction = instruction[0]
        #The number of steps to move in that direction
        steps = int(instruction[1:len(instruction)])
        #Move horizontally

        horizontal_steps = direction[current_direction][0] * steps
        vertical_steps = direction[current_direction][1] * steps
        
        #We are going to sum N times the direction steps to points_it_has_passed
        times_to_iterate = abs(horizontal_steps if horizontal_steps != 0 else vertical_steps)

        for j in range(0,times_to_iterate):
            last_point_passed = points_it_has_passed[len(points_it_has_passed) - 1]
            to_add = sum_two_arrays(last_point_passed, direction[current_direction])
            points_it_has_passed.append(to_add)
            
    
    return points_it_has_passed


