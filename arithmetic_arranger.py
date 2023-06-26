def arithmetic_arranger(problems, solve = False):
  size = len(problems) # Guarda a quantia de problemas
  limit = 5 # Limite do número de problemas
  op = ('+','-') # Operações válidas
  max_digits = 4 # Quantia máxima de dígitos presentes em um número
  
  if(size > limit):
    return 'Error: Too many problems.'
  else:
    total_digits = size * [0] # Guarda o número de digitos dos resultados de todos os problemas
    digits_1 = size * [0] # Guarda o número de digitos dos primeiros operandos de todos os problemas
    digits_2 = size * [0] # Guarda o número de digitos dos segundos operandos de todos os problemas
    for count in range(size):
      problems[count] = problems[count].split()
      if(problems[count][1] not in op): # Verifica se a operação do problema é válida
        return "Error: Operator must be '+' or '-'."
      elif(not problems[count][0].isnumeric() or not problems[count][2].isnumeric()): # Verifica se os operandos estão em formato numérico
        return 'Error: Numbers must only contain digits.'
      else:
        digits_1[count] = len(problems[count][0])
        digits_2[count] = len(problems[count][2])
        if(digits_1[count] > max_digits or digits_2[count] > max_digits): # Verifica se a quantia de dígitos dos operandos não excede o limite
          return 'Error: Numbers cannot be more than four digits.'
        else:
          if(digits_1[count] > digits_2[count]):
            total_digits[count] += 2 + digits_1[count]
          else:
            total_digits[count] += 2 + digits_2[count]
    
    lines = 3
    if(solve == True): # Caso o resultado dos problemas seja requisitado, será adicionado mais uma linha no output
      lines += 1
      
    arranged_problems = '' # Guarda o output da função
    for line in range(lines):
      for count in range(0, size): # Repetição para cada problema
        if(line == 0): # Na primeira linha é gerado o primeiro operando
          space = ' ' * (total_digits[count] - digits_1[count])
          arranged_problems += space + problems[count][0]
        elif(line == 1): # # Na segunda linha é gerado a operação ao lado do segundo operando
          space = ' ' * (total_digits[count] - digits_2[count] - 1)
          arranged_problems += problems[count][1] + space + problems[count][2]
        elif(line == 2): # Na terceira linha é gerado uma divisória
          arranged_problems += '-' * total_digits[count]
        else: # Caso haja uma quarta linha
          if(problems[count][1] == op[0]): # Caso a operação seja '+', gera o resultado da soma
            answer = int(problems[count][0]) + int(problems[count][2])
          else: # Caso a operação seja '-', gera o resultado da subtração
            answer = int(problems[count][0]) - int(problems[count][2])
          space = ' ' * (total_digits[count] - len(str(answer)))
          arranged_problems += space + str(answer)
        if(count != size-1):
          arranged_problems += '    '
      if(line != lines-1):
        arranged_problems += '\n'
    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
