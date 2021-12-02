import machine, onewire, ds18x20, time
import os
import ESP8266WebServer

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))



def read_ds_sensor():
    roms = ds_sensor.scan()
    print('Found DS devices: ', roms)
    print('Temperatures: ')
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        if isinstance(temp, float):
            msg = round(temp)
            print(temp, end=' ')
            print('Valid temperature')

            return msg
    return b'0.0'



def index(socket, args):
    ESP8266WebServer.ok(socket, "200", "index.html")
    
def table(socket, args):
    ESP8266WebServer.err(socket, "200", "table.html")
def chart(socket, args):
    ESP8266WebServer.ok(socket, "200", "chart.html")
    
ESP8266WebServer.begin(80)
ESP8266WebServer.onPath("/index.html", index)
ESP8266WebServer.onPath("localhost/table.html", table)
ESP8266WebServer.onPath("localhost/chart.html", chart)

ESP8266WebServer.setDocPath("/")
while True:
    ESP8266WebServer.handleClient()
    read_ds_sensor()
    time.sleep(10)