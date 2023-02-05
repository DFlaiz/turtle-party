# By Doris Flaiz
# Turtle play
import turtle
from random import randint

bg = turtle.Screen()
bg.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.penup()
turtle.back(200)
turtle.pendown()
turtle.pensize(4)
# using 10 different colors
colors = ['red', 'purple','blue', 'pink', 'green', 'orange', 'yellow', 'teal','magenta','white']

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

def draw(num):
    for n in range(3, 13):
        turtle.begin_fill()
        turtle.pencolor(colors[n%10])
        turtle.left(360 /20)
        back(num)
        polygon(n, 150 / n)

def moveright(go):
    turtle.penup()
    turtle.forward(go)
    turtle.pendown()

def movedown(go2):
    turtle.penup()
    turtle.right(90)
    turtle.forward(go2)
    turtle.right(90)
    turtle.forward(150)
    turtle.pendown()

def back(len2):
  turtle.penup()
  turtle.backward(len2)
  turtle.pendown()

def main():
    draw(25)
    turtle.right(90)
    draw(25)
    turtle.right(90)
    draw(25)
    turtle.right(90)
    draw(25)

main()

turtle.Screen().exitonclick()


# def rectangle(long,short):
#     for r in range(2):
#         turtle.forward(long)
#         turtle.left(90)
#         turtle.forward(short)
#         turtle.left(90)
#
#
# def triangle(side):
#     for t in range(3):
#         turtle.right(120)
#         turtle.forward(side)
#
# turtle.color('red')

# rectangle(90, 90)
# moveright(135)
# turtle.color('purple')
# rectangle(150, 90)
# movedown(100)
# turtle.color('blue')
# triangle(80)
# back(150)
# turtle.color('green')
# triangle(100)
# back(300)
# movedown(25)

