def decode(arr_input, input_noun, input_verb):
  #We must made a copy of the array, to avoid changing the original
  arr_copy = arr_input.copy()
  arr_copy[1] = input_noun
  arr_copy[2] = input_verb
  counter = 0
  

  while counter < len(arr_copy):
        #Check the operation, the second and third parameters and their future position
        current_code =  arr_copy[counter] #opcode
        first = arr_copy[counter+1]
        second = arr_copy[counter+2]
        place = arr_copy[counter+3]
        
        
        if current_code == 1:
          arr_copy[place] = arr_copy[first] + arr_copy[second]
          counter += 4
        elif current_code == 2:
          arr_copy[place] = arr_copy[first] * arr_copy[second]
          counter += 4
        elif current_code == 99:
          break
        else:
          break
  return arr_copy[0]


def run_decoder(input_list, output):
  for noun in range(100):
    for verb in range(100):
      if decode(input_list, noun, verb) == output:
        return (100 * noun) + verb
  return -1