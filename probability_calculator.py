import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = list() 
    for color, num in kwargs.items(): # Repetição para inserir as bolas na lista
      self.contents += num * [color]

  def draw(self, num): # Método para retirar aleatoriamente um determinado número de bolas
    qnt = len(self.contents) # Quantidade de bolas
    out = list() # Lista com as bolas retiradas
    if(num >= qnt): # Caso o número seja maior que a quantia de bolas, retorna toda a lista e a esvazia
      out = self.contents
      self.contents = []
    else:
      for i in range(num):
        index = random.randint(0, qnt-1) # Seleciona uma posição aleatória da lista
        out.append(self.contents[index])
        del self.contents[index]
        qnt -= 1
    return out
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments): # Função que retorna a probabilidade de retirar uma porção de bolas desejavadas                                                                                                                             # com base na quantidade de bolas que podem ser retiradas por vez e no número de testes
  successes = 0
  exp = list()
  for color, num in expected_balls.items(): # Insere as bolas desejadas na lista
    exp += num * [color]
    
  for x in range(num_experiments):
    cp1 = copy.deepcopy(hat) # Cópia do 'hat' com as bolas disponíveis
    cp2 = copy.copy(exp) # Cópia da lista com as bolas desejadas
    out = cp1.draw(num_balls_drawn) # As bolas retiradas do 'hat'
    
    for ball in out:
      if(ball in cp2):
        cp2.remove(ball) # Remove a bola da lista caso tenha sido retirada do 'hat'

    if(cp2 == []): # Caso a lista de bolas desejadas esteja vazia, então é dado como sucesso
      successes += 1
  return successes / num_experiments # Retorna a quantia de testes com sucesso dividido pelo número de experimentos usados


hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print(probability)