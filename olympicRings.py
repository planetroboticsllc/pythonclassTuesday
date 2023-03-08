from turtle import *

radius = 100
dist = 2 * radius + 20
pensize(7)

# circle 1
penup()
goto(-200, 100)
pendown()
circle(radius)

# circle 2
penup()
forward(dist)
pendown()
circle(radius)

# circle 3
penup()
forward(dist)
pendown()
circle(radius)

# circle 4
penup()
goto(-200 + radius, 100 - radius)
pendown()
circle(radius)

# circle 5
penup()
forward(dist)
pendown()
circle(radius)

done()
