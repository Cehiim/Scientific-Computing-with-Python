class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)
  
  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2*self.width) + (2*self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if(self.width > 50 or self.height > 50):
      return "Too big for picture."
    else:
      fig = ''
      line = '*' * self.width + '\n'
      for i in range(self.height):
        fig += line
      return fig

  def get_amount_inside(self, shape):
    amount_width = self.width // shape.width
    amount_height = self.height // shape.height
    if(amount_width > 0 and amount_height > 0):
      return amount_height * amount_width
    else:
      return 0


class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return 'Square(side={})'.format(self.width)

  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side
  
  def set_width(self, new_width):
    self.width = new_width
    self.height = new_width

  def set_height(self, new_height):
    self.width = new_height
    self.height = new_height


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