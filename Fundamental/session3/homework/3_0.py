from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey' ]
speed(-1)
# for i in range(len(colors)):
#     color(colors[i])

for edge in range(3, 8):
    color(colors[edge-3])
    for i in range(edge):
        forward(100)
        left(360/edge)
mainloop()