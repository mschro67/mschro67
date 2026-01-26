#by mschro67

#pin 0: led

from machine import Pin

Pin(0,Pin.OUT).toggle()
