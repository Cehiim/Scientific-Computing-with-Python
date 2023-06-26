def add_time(start, duration, day = None):
  period = start.split()
  time = period[0].split(':')
  total_min = int(time[1]) # Guarda os minutos do horário inicial
  total_hr = int(time[0]) # Guarda as horas do horário inicial

  period = period[1] # Guarda o período inicial
  periods = ('AM', 'PM')
  pos = periods.index(period) # Guarda a posição do período inicial
  
  time = duration.split(':')
  total_min += int(time[1]) # Soma os minutos a serem adicionados
  total_hr += int(time[0]) # Soma as horas a serem adicionadas

  extra = 0
  if(total_min >= 60): # Caso o total de minutos seja maior ou igual a 60, separa os minutos adicionais e converte em horas numa variável auxiliar
    extra = total_min // 60
    total_min %= 60

  total_hr += extra # É adicionado as horas extras
  extra = 0
  if(total_hr >= 12): # Caso o total de horas seja maior ou igual a 12, separa as horas adicionais e converte em períodos numa variável auxiliar
    extra = total_hr // 12
    total_hr %= 12
  if(total_hr == 0):
    total_hr = 12

  pos += extra # Acrescenta os períodos adicionais
  extra = 0
  if(pos > 1): # Caso a posição do período final seja maior que o tamanho da tupla de períodos, guarda o período final e converte os períodos adionais em dias
    extra = pos // 2 # Guarda a quantia de dias adiocionais
    pos %= 1
  period = periods[pos] # Guarda o período final

  if(day != None):
    day = day.capitalize() # Formata o input do dia
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    if(day in days):
      pos = days.index(day) # Guarda a posição do dia inicial
      pos += extra # Acrescenta os dias adiocionais
      if(pos > 6):
        pos %= 7
      day = days[pos] # Guarda o dia final
  
  if(extra == 0):
    extra = ''
  elif(extra == 1):
    extra = ' (next day)'
  else:
    extra = ' ({} days later)'.format(extra)
    
  if(day == None):
    new_time = '{}:{:02d} '.format(total_hr, total_min) + period + extra
  else:
    new_time = '{}:{:02d} '.format(total_hr, total_min) + period + ', ' + day + extra
  
  return new_time


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
