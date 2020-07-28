from turtle import *
speed(0)
color('blue')
left(130)
for i in range(50):
    for j in range(3):
        forward(100 - 2*i)
        left(90)
    forward(100 - 2*i)
    left(80)
mainloop()