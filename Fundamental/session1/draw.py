from turtle import *

speed(-1)
shape('turtle')
color('green')

number = int(input())
for i in range(number):
    forward(100)
    left(360/number)

mainloop()