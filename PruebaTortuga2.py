import turtle
t=turtle.Turtle()
t.speed(0)
t.shape("turtle")
for i in range(50):
    t.circle(50)
    t.forward(1)
    t.right(10)
turtle.done()