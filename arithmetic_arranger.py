def arithmetic_arranger(problems, solve = False):
  size = len(problems)
  limit = 5
  op = ('+','-')
  max_digits = 4
  
  if(size > limit):
    return 'Error: Too many problems.'
  else:
    total_digits = size * [0]
    digits_1 = size * [0]
    digits_2 = size * [0]
    for count in range(size):
      problems[count] = problems[count].split()
      if(problems[count][1] not in op):
        return "Error: Operator must be '+' or '-'."
      elif(not problems[count][0].isnumeric() or not problems[count][2].isnumeric()):
        return 'Error: Numbers must only contain digits.'
      else:
        digits_1[count] = len(problems[count][0])
        digits_2[count] = len(problems[count][2])
        if(digits_1[count] > max_digits or digits_2[count] > max_digits):
          return 'Error: Numbers cannot be more than four digits.'
        else:
          if(digits_1[count] > digits_2[count]):
            total_digits[count] += 2 + digits_1[count]
          else:
            total_digits[count] += 2 + digits_2[count]
    
    lines = 3
    if(solve == True):
      lines += 1
      
    arranged_problems = ''
    for line in range(lines):
      for count in range(0, size):
        if(line == 0):
          space = ' ' * (total_digits[count] - digits_1[count])
          arranged_problems += space + problems[count][0]
        elif(line == 1):
          space = ' ' * (total_digits[count] - digits_2[count] - 1)
          arranged_problems += problems[count][1] + space + problems[count][2]
        elif(line == 2):
          arranged_problems += '-' * total_digits[count]
        else:
          if(problems[count][1] == op[0]):
            answer = int(problems[count][0]) + int(problems[count][2])
          else:
            answer = int(problems[count][0]) - int(problems[count][2])
          space = ' ' * (total_digits[count] - len(str(answer)))
          arranged_problems += space + str(answer)
        if(count != size-1):
          arranged_problems += '    '
      if(line != lines-1):
        arranged_problems += '\n'
    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
