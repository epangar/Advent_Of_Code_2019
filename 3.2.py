#class for points it has passed through
class Point:
  def __init__(self, current_point, steps_to_get_there):
    self.current_point = current_point
    self.steps_to_get_there = steps_to_get_there


def distance(first, second):
    
    start = [0,0]
    
    final_first = list(map(lambda x: {
      'Current':x.current_point,
      'Steps' : x.steps_to_get_there
      }, move_through_matrix(first, start)))
    
    final_second = list(map(lambda x: {
      "Current":x.current_point,
      "Steps" : x.steps_to_get_there
      }, move_through_matrix(second, start)))
    

    #Equal_points   
    equal_points = []
    for k in range(1, len(final_first)):
      point = final_first[k]['Current']
      steps = final_first[k]['Steps']
      does_point_exist_in_second = list(filter(lambda obj: obj['Current'][0]==point[0] and obj['Current'][1]==point[1], final_second))
      
      if(len(does_point_exist_in_second) > 0):
        
      
        second_steps = does_point_exist_in_second[0]['Steps']
        
        equal_points.append({
        "Intersection":point,
        "Steps" : steps + second_steps
        })
        

    equal_points.sort(key = lambda inter:inter['Steps'])
    
    shortest = equal_points[0]
    
    return shortest['Steps']

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

    total_steps = 0

    current_start = Point(point_to_move.copy(), total_steps)
    points_it_has_passed = [current_start]
    
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
          total_steps += 1
          last_point_passed = points_it_has_passed[len(points_it_has_passed) - 1]
          to_add = sum_two_arrays(last_point_passed.current_point, direction[current_direction])
          coordinate = Point(to_add, total_steps)
          points_it_has_passed.append(coordinate)
            
    
    return points_it_has_passed



