#by mschro67
#for Raspberry Pi Pico

try:
  from machine import Pin
  from time import sleep

  led=Pin(25,Pin.OUT) #onboard led on RPI Pico 2

  while True:
    led.toggle
    sleep(0.2)
except ModuleNotFoundError:
  print("Module(s) not found!")
except Exception as e:
  print(f"Error: {e}!")
