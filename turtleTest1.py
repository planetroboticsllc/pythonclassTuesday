from turtle import *

color("red", "yellow")
pensize(5)

begin_fill()
i = 0
sides = 8
while i < sides:
    forward(100)
    left(360/sides)
    i = i + 1

end_fill()
done()
