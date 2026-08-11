import turtle
t=turtle.Turtle()
t.speed(10)
t.shape("turtle")
t.right(150)
for i in range(50):
    t.circle(20)
    t.backward(50)
    t.left(50)
turtle.done()