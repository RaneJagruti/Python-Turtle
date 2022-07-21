import turtle
turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
turtle.title("Circle Circle")
for i in range (300):
    for colours in ['red','magenta','blue','cyan','green','yellow','white']:
        turtle.color(colours)
        turtle.forward(i*3)
        turtle.left(90)
     
