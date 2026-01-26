#by mschro67
#for microcontroller with WLAN chip

import network
import socket
import time
from machine import I2C,Pin,ADC

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

def read_temp():
  reading = sensor_temp.read_u16() * conversion_factor
  temperature_c = 27 - (reading - 0.706) / 0.001721
  return temperature_c

essid="[WLAN-NAME]"
password="[PASSWORD]"
print(f"name: {essid}")
print(f"password: {password}")

ap = network.WLAN(network.AP_IF)
ap.config(essid=essid, password=password)
ap.active(True)

while not ap.active():
  time.sleep(1)

print("activated acces point")
print(f"ip-adress: {ap.ifconfig()[0]}")

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)
print("waiting for requests...")
while True:
  try:
    temp = read_temp()
    print()
    print(f"temperature: {temp:.2f}°C")
    html = f"""
      <!DOCTYPE html>
      <html>
        <head>
          <title>[ADD TITLE HERE]</title>
          <meta charset="utf8">
        </head>
        <body>
          <p>
            [ADD TEXT HERE]
            <h2>Temperatur</h2>
            {temp:.2f}°C
            <br>
            Reload the website to get the new themperature.
          </p>    
        </body>
      </html>
    """
    cl,addr = s.accept()
    print("connected to", addr)
    request = cl.recv(1024)
    request = str(request)
    print(f"request: {request}")
    cl.send('HTTP/1.1 200 OK\r\n')
    cl.send('Content-Type: text/html\r\n')
    cl.send('Connection: close\r\n\r\n')
    cl.sendall(html)
    cl.close()
    print("answer sent!")
  except Exception as e:
    print(f"error: {e}")
    if 'cl' in locals():
      try:
        cl.close()
      except:
        pass
