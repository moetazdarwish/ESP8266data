logic_state = bt.value()

if logic_state==True:
import uos, machine , time
import ESP8266WebServer
from machine import Pin
try:
  import usocket as socket
except:
  import socket
import network
import gc
gc.collect()

ap = network.WLAN(network.AP_IF)

ap.active(False)

led = Pin(13, Pin.OUT)

bt = Pin(12 , Pin.IN)

ssid = 'MicroPython-AP'

for i in range (5):
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)

ap = network.WLAN(network.AP_IF)

ap.active(True)

ap.config(essid=ssid)

while ap.active() == False:

  pass

print('Connection successful')

print(ap.ifconfig())

def index(socket, args):

    ESP8266WebServer.ok(socket, "200", "index.html")

def table(socket, args):

    ESP8266WebServer.err(socket, "200", "table.html")

ESP8266WebServer.begin(80)
ESP8266WebServer.onPath("/index.html", index)
ESP8266WebServer.onPath("localhost/table.html", table)
ESP8266WebServer.onPath("localhost/chart.html", index)
ESP8266WebServer.setDocPath("/")
print("server start")
while True:

    

    ESP8266WebServer.handleClient()
