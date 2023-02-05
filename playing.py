# # Going down the rabbit hole :)
# By Doris Flaiz
import turtle
#making the background black

bg = turtle.Screen()
bg.bgcolor("black")
turtle.speed("fast")
# using 7 different colors
colors = ['red', 'purple','blue', 'green', 'orange', 'yellow', 'teal']

def spiral(circle):
  for x in range(circle):
    turtle.pencolor(colors[x%6])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)
  turtle.pencolor("red")
  turtle.forward(x/2)

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

spiral(360)
move(500)
turtle.left(90)


for n in range(3, 10):
  turtle.pencolor(colors[n%7])
  move(15)
  polygon(n, 100/n)
  back(15)
  turtle.right(360/7)


turtle.Screen().exitonclick()