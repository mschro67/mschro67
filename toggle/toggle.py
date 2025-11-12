from machine import Pin
with open("toggle/value.txt","r") as v:
    if int(v.read())==1:
        Pin(1,Pin.OUT).value(1)
        with open("toggle/value.txt","w") as w:
            w.write("0")
    else:
        Pin(1,Pin.OUT).value(0)
        with open("toggle/value.txt","w") as w:
            w.write("1")