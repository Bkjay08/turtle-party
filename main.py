# Turtle Party Project
# by James Middleton

import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def move(len):
  back(-1 * len)

#Repeat 3 times
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
for n in range(3, 10):
  move(50) #forward
  polygon(n, 100 / n)
  back(50)
  turtle.right(360 / 7)
