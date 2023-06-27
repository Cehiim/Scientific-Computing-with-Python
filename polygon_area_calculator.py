class Rectangle:
  def __init__(self, width, height):
    self.width = width # Largura
    self.height = height # Altura

  def __str__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)
  
  def set_width(self, new_width): # Método para mudar o valor da largura
    self.width = new_width

  def set_height(self, new_height): # Método para mudar o valor da altura
    self.height = new_height

  def get_area(self): # Método para retornar o valor da área
    return self.width * self.height

  def get_perimeter(self): # Método para retornar o valor do perímetro
    return (2*self.width) + (2*self.height)

  def get_diagonal(self): # Método para retornar o valor da diagonal
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self): # Método para retornar um exemplo visual do formato
    if(self.width > 50 or self.height > 50): # Não retorna caso a figura seja maior que 50 unidades, tanto para largura quanto para a altura
      return "Too big for picture."
    else:
      fig = ''
      line = '*' * self.width + '\n'
      for i in range(self.height):
        fig += line
      return fig

  def get_amount_inside(self, shape): # Método para retornar o número de vezes que outro formato pode caber
    amount_width = self.width // shape.width
    amount_height = self.height // shape.height
    if(amount_width > 0 and amount_height > 0):
      return amount_height * amount_width
    else:
      return 0


class Square(Rectangle):
  def __init__(self, side): # Por ser um quadrado, a largura e altura têm o mesmo valor
    self.width = side
    self.height = side

  def __str__(self):
    return 'Square(side={})'.format(self.width)

  def set_side(self, new_side): # Método para mudar o valor dos lados
    self.width = new_side
    self.height = new_side
  
  def set_width(self, new_width): # O método foi alterado de acordo com as propriedades de um quadrado
    self.width = new_width
    self.height = new_width

  def set_height(self, new_height): # O método foi alterado de acordo com as propriedades de um quadrado
    self.width = new_height
    self.height = new_height


#Exemplos
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
