import turtle

t = turtle.Turtle()
t.speed(10)  # Fastest speed

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for x in range(180):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()