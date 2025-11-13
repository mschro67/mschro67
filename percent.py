#by mschro67

while True:
  try:
    points=float(input("Your points: "))
    max=float(input("Maximum points: "))

    print(f"{points}/{max} points: {points/max*100:.2f}%")
    break
  except:
    print("Only type numbers!")
    print()
