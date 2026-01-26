#by mschro67
#for the Orpheus Pico

#pin 23: button
#pin 25: led

from machine import Pin
from time import sleep

button=Pin(23,Pin.IN,Pin.PULL_UP)
led=Pin(25,Pin.OUT)

while True:
  if button.value() == 0:
    led.toggle()
    sleep(0.3)
