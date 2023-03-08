from turtle import *

i = 1
pensize(2)
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(135)
    # stop the loop if absolute position of the cursor
    # is closer to 0
    if abs(pos()) < 1:
        break

end_fill()

penup()
goto(-200, -100)
pendown()
color("black", "brown")
i = 0
sides = 3
begin_fill()
while i < sides:
    forward(100)
    left(360/sides)
    i = i + 1

end_fill()

penup()
goto(-200, 200)
pendown()
circle(100)

done()
