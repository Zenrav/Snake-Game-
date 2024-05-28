from turtle import Turtle
import random
colour=['white','gold','orange']
class Food(Turtle):
   def __init__(self):
    super().__init__()
    self.shape('circle')
    self.penup()
    self.shapesize(stretch_len=1,stretch_wid=0.5)
    self.color(random.choice(colour))
    self.speed('fastest')
   
   def refresh(self):
      x_cor=random.randint(-280,280)
      y_cor=random.randint(-280,280)
      self.goto(x_cor,y_cor)
      self.color(random.choice(colour))
   
      