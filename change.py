#by mschro67

from machine import Pin

with open("number.txt","r") as d:
  a=int(d.read())
  Pin(a,Pin.OUT).value(0)
  a+=1
  if a>4:
    a=1
  Pin(a,Pin.OUT).toggle()
  with open("number.txt","w") as b:
    b.write(str(a))

"""
This code saves a naumber in a text file and acts depending on its content after starting.
This is a way to safe data from the program after restarting.
"""
