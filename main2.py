import machine, onewire, ds18x20, time , esp
import os
import ESP8266WebServer

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))



def read_ds_sensor():
    
    roms = ds_sensor.scan()
    
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        msg = (temp)
        return msg
    return b'0.0'


    
def tablewrite():
    temp = read_ds_sensor()
    f = open("table.html","a")
    print ("f 0pen")
    f.write(str(count)+","+temp+"\n")
    count +=1
    f.close
    
def reading(temp):
    temp = read_ds_sensor()
    file = open("/reading.txt","w")
    file.write(str(temp))
    file.close
    

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
temp = read_ds_sensor()
i = 0
msg = read_ds_sensor()
rtc = machine.RTC()
rtc.datetime((2020, 10, 21, 2, 10, 32, 0, 0))
while True:
    ESP8266WebServer.handleClient()
    
    #read_ds_sensor()
    #time ()
    #reading(temp)
    
    t = time.gmtime()
    
    
    d = t[:8]
    print(d)
    mk = time.mktime(d)
    print(mk)
    #t1 = t[3:5]
    #t2 = str(t1)
    #t3 = str.replace(",",":")
    #t2  = t1[0]
    #t3 = t1 [1]
    #t4 = str(t2)+":"+str(t3)
    #d1 = d[0]
    #d2 = d[1]
    #d3 = d[2]
    #ds = str(d1)+"/"+str(d2)+"/"+str(d3)
   
    
   
    #temp = read_ds_sensor()
    #temp1= (temp*10)
    #R1 = str(temp1)
    #R = ds+"-"+t4
    #N = i*0.2
    #M = str(N)
    #f2 = open('chart.html','a')
    #f2.write("<li class='data-point'onclick='S(this)'style='bottom:"+R1+"px; left:"+M+"px'1`;"" data-type="" "+R+"-"+str(temp)+"C></li>"+'\n')
    #f2.close()
    #i +=1
    #f = open('table.html','a')
    
    #f.write("<tr><td>"+ds+"-"+t4+"</td><td>"+temp+"</tr>"+'\n')
    #f.close()
    
    time.sleep(5)
    
   