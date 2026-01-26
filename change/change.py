#by mschro67
#v2

#pin 0-4: led

from machine import Pin

with open("change/number.txt","r") as d:
    a=int(d.read())
    Pin(a,Pin.OUT).value(0)
    a+=1
    if a>4:
        a=0
    else:
        Pin(a,Pin.OUT).toggle()
    with open("change/number.txt","w") as b:

        b.write(str(a))
