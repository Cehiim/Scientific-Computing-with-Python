class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  
  def deposit(self, amount, description = ''):
    self.ledger.append({"amount": amount, "description": description})

  
  def withdraw(self, amount, description = ''):
    if(self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  
  def get_balance(self):
    total = 0
    for i in self.ledger:
      total += i.get("amount")
    return total

  
  def transfer(self, amount, destination):
    msg = "Transfer to " + destination.name
    if(self.withdraw(amount, msg)):
      msg = "Transfer from " + self.name
      destination.deposit(amount, msg)
      return True
    else:
      return False

  
  def check_funds(self, amount):
    total = self.get_balance()
    if(amount > total):
      return False
    else:
      return True

  
  def __str__(self):
    msg = self.name.center(30, '*') + '\n'
    
    for i in self.ledger:
      description = i.get("description")[0:23]
      amount = '{:.2f}'.format(i.get("amount"))
      msg += description.ljust(23) + amount.rjust(7) + '\n'

    msg += 'Total: ' + '{:.2f}'.format(self.get_balance())
    return msg




def create_spend_chart(categories):
  size = len(categories)
  total_spend = 0
  spend_list = [0] * size
  for i in range(size):
    for j in range(len(categories[i].ledger)):
      amount = categories[i].ledger[j].get("amount")
      if(amount < 0):
        total_spend += abs(amount)
        spend_list[i] += abs(amount)

  msg = "Percentage spent by category\n"
  for i in range(100, -10, -10):
    aux = str(i) + '|'
    msg += aux.rjust(4)
    for j in range(size):
      if(spend_list[j]/total_spend >= i/100):
        msg += ' o '
      else:
        msg += '   '
    msg += ' \n'
  aux = '---' * size
  msg += '    ' + aux + '-' + '\n'

  max = 0
  for i in range(size):
    aux = categories[i].name
    aux = len(aux)
    if(aux > max):
      max = aux
  for i in range(max):
    msg += '    '
    for j in range(size):
      aux = categories[j].name
      try:
        msg += aux[i].center(3)
      except:
        msg += '   '
    if(i < max-1):
      msg += ' \n'
    else:
      msg += ' '
  return msg


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))
