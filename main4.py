import machine, onewire, ds18x20, time , esp
import os




ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))


rtc = machine.RTC()
rtc.datetime((2020, 10, 21, 2, 10, 32, 0, 0))



def read_ds_sensor():
    
    roms = ds_sensor.scan()
    
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        msg = (temp)
        return msg
    return b'0.0'



    
def reading(temp):
    temp = read_ds_sensor()
    file = open("/reading.txt","w")
    file.write(str(temp))
    file.close
    


#ESP8266WebServer.begin(80)
#ESP8266WebServer.onPath("/index.html", index)
#ESP8266WebServer.onPath("localhost/table.html", table)
#ESP8266WebServer.onPath("localhost/chart.html", chart)

    #f.write("<tr><td>"+ds+"-"+t4+"</td><td>"+temp+"</tr>"+'\n')
    #f.close()





#sleep for 10 seconds (10000 milliseconds)
   
print ('i here')
t = time.gmtime()
d = t[:3]
t1 = t[3:5]
t2 = str(t1)
#t3 = str.replace(",",":")
t2  = t1[0]
t3 = t1 [1]
t4 = str(t2)+":"+str(t3)
d1 = d[0]
d2 = d[1]
d3 = d[2]
ds = str(d1)+"/"+str(d2)+"/"+str(d3)
g = open('r.txt','r')
l = g.read()
g.close()
x = float(l)
k = x + 0.2
g = open('r.txt','w')
g.write(str(k))
g.close()
temp = read_ds_sensor()
temp1= (temp*10)
R1 = str(temp1)
R = ds+"-"+t4
M = str(k)
f2 = open('chart.html','a')
f2.write("<li class='data-point'onclick='S(this)'style='bottom:"+R1+"px; left:"+M+"px';"" data-type="" "+R+"-"+str(temp)+"C></li>"+'\n')
f2.close()
    #i +=1
    #f = open('table.html','a')
time.sleep(5)   
    #f.write("<tr><td>"+ds+"-"+t4+"</td><td>"+temp+"</tr>"+'\n')
    #f.close()
print('Im awake, but Im going to sleep')




#while True:
    
    #ESP8266WebServer.handleClient()
    
    #read_ds_sensor()
    #time ()
    #reading(temp)
 