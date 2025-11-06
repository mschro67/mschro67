#by mschro67

try:
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
except ModuleNotFoundError:
  print("Module not found!")
except Exception as e:
  print(f"Error {e}!")
