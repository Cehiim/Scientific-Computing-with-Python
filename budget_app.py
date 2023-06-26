class Category:
  def __init__(self, name):
    self.name = name # Nome da categoria
    self.ledger = list() # Lista que servirá para registrar a contabilidade da categoria

  
  def deposit(self, amount, description = ''): # Método para depositar um determinado valor numa categoria, a descrição é opcional
    self.ledger.append({"amount": amount, "description": description})

  
  def withdraw(self, amount, description = ''): # Método para retirar um determinado valor numa categoria, a descrição é opcional
    if(self.check_funds(amount)): # A ação só será feita caso o valor a ser retirado não seja maior que o saldo da categoria
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  
  def get_balance(self): # Método para calcular o valor total de uma categoria
    total = 0
    for i in self.ledger:
      total += i.get("amount")
    return total

  
  def transfer(self, amount, destination): # Método para transferir um determinado valor de uma categoria para outra
    msg = "Transfer to " + destination.name
    if(self.withdraw(amount, msg)): # Retira o valor da categoria de origem
      msg = "Transfer from " + self.name
      destination.deposit(amount, msg) # Deposita o valor para a categoria de destino
      return True
    else:
      return False

  
  def check_funds(self, amount): # Método para checar se é possível retirar um determinado valor sem negativar o saldo de uma categoria
    total = self.get_balance()
    if(amount > total):
      return False
    else:
      return True

  
  def __str__(self): # Método para imprimir a lista de contabilidade de uma categoria
    msg = self.name.center(30, '*') + '\n' # Título
    
    for i in self.ledger: # Nessa repetição são listadas as ações efetuadas na categoria
      description = i.get("description")[0:23]
      amount = '{:.2f}'.format(i.get("amount"))
      msg += description.ljust(23) + amount.rjust(7) + '\n'

    msg += 'Total: ' + '{:.2f}'.format(self.get_balance()) # Saldo da categoria
    return msg




def create_spend_chart(categories): # Função para imprimir um gráfico apresentando a porcentagem gasta de cada categoria listada
  size = len(categories)
  total_spend = 0
  spend_list = [0] * size
  for i in range(size):
    for j in range(len(categories[i].ledger)):
      amount = categories[i].ledger[j].get("amount")
      if(amount < 0):
        total_spend += abs(amount) # É registrado os gasto total
        spend_list[i] += abs(amount) # É registrado os gasto em cada categoria

  msg = "Percentage spent by category\n" # Título
  for i in range(100, -10, -10): # Nessa repetição é gerado os valores do eixo Y
    aux = str(i) + '|'
    msg += aux.rjust(4)
    for j in range(size): # Nessa repetição é gerado as barras
      if(spend_list[j]/total_spend >= i/100):
        msg += ' o '
      else:
        msg += '   '
    msg += ' \n'
    
  aux = '---' * size
  msg += '    ' + aux + '-' + '\n'
  max = 0
  for i in range(size): # Nessa repetição mede o tamanho dos nomes das categorias e registra o maior
    aux = categories[i].name
    aux = len(aux)
    if(aux > max):
      max = aux
  for i in range(max): # Nessas repetições é gerado o nome das categorias de forma vertical
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
