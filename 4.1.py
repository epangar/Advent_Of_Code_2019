def two_adjacents_are_the_same(input_str):
  number_of_adjacents = 0

  LEN = len(input_str)
  for c in range(0, LEN):
    
    if c < LEN-1:
      char = input_str[c]
      next = input_str[c+1]
      
      if char == next:
        number_of_adjacents += 1
  
  #At least two adjacents are the same
  return number_of_adjacents > 0

def digits_never_decrease(str_input):

  LEN = len(str_input)
  for c in range(0, LEN):
    if c < LEN-1:
      char = str_input[c]
      next = str_input[c+1]
      
      if ord(char) > ord(next):
        return False
  return True


def count_between_range(start, end):

  answer = 0

  for j in range(start, end):
    str_n = str(j)

    if two_adjacents_are_the_same(str_n) and digits_never_decrease(str_n):
      answer += 1
  
  return answer