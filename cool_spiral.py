# Turtle Party Project
# By Doris Flaiz
# 09.27.22
import turtle
turtle.color('red')

colors = ['red', 'purple','blue', 'green', 'orange', 'yellow', 'black']
# #t = turtle.Pen()
# #turtle.bgdcolor = "black"

# for x in range(360):
#   turtle.pencolor(colors[x%6])
#   turtle.width(x/100+1)
#   turtle.forward(x)
#   turtle.left(59)

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
    
# forward helper function
def move(len):
  back(-1 * len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
for n in range(3, 10):
  turtle.pencolor(colors[n%7])
  move(10)
  polygon(n, 100/n)
  back(10)
  turtle.right(360/7)

    
# def spiral(len, angle):
#   for i in range(len, 5, -5):
#     turtle.forward(i)
#     turtle.right(anle)
    
# spiral(75,45)
