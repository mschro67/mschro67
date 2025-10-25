import turtle
t=turtle.Turtle()

while True:
    t.reset()
    a=int(input("Length: "))
    b=int(input("Edges: "))
    for i in range(b):
        t.forward(a)
        t.left(360/b)
    print()
