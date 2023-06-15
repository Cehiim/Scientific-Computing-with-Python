def add_time(start, duration, day = None):
  period = start.split()
  time = period[0].split(':')
  total_min = int(time[1])
  total_hr = int(time[0])

  period = period[1]
  periods = ('AM', 'PM')
  pos = periods.index(period)
  
  time = duration.split(':')
  total_min += int(time[1])
  total_hr += int(time[0])

  extra = 0
  if(total_min >= 60):
    extra = total_min // 60
    total_min %= 60

  total_hr += extra
  extra = 0
  if(total_hr >= 12):
    extra = total_hr // 12
    total_hr %= 12
  if(total_hr == 0):
    total_hr = 12

  pos += extra
  extra = 0
  if(pos > 1):
    extra = pos // 2
    pos %= 1
  period = periods[pos]

  if(day != None):
    day = day.capitalize()
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    if(day in days):
      pos = days.index(day)
      pos += extra
      if(pos > 6):
        pos %= 7
      day = days[pos]
  
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