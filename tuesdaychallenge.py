# By Doris Flaiz
# Tuesday Coding Challenge
# 2-6-2023

import turtle
turtle.bgcolor("black")
turtle.speed(-5)
turtle.pensize(4)
# using 12 different color
for i in range(2):  #looping throught these colors twice
    for color in ['red', 'purple','blue', 'pink', 'green', 'orange', 'yellow', 'teal','magenta','white','cyan','brown']:
        turtle.pencolor(color) #setting the pen color
        turtle.left(15)  # turning the angle for the draw around the circle, so that the beginning and end meet perfectly
        for square in range(4):  #drawing the square... four sides at a 90 degree angle for a length of 200
            turtle.left(90)
            turtle.forward(300)

turtle.Screen().exitonclick()  #have to manually close the window so that you can seen the output image