import machine, onewire, ds18x20, time 
import os
from machine import Pin

led = Pin(5, Pin.OUT)
for i in range(5):
    led.high()
    time.sleep(0.2)
    led.low()
    time.sleep(0.2 )

f = open ('time.txt','r')
fs=f.read()
f.close()
d = fs[:2]
m = fs[3:5]
y = fs[6:11]
hs = fs[14:16]
ms = fs[18:20]
year = int(y)
month = int(m)
date = int(d)
h = int(hs)
m = int(ms)
Days_in_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 1
while days > 0:
   m += 15
   if m > 60:
       h += 1
       if h > 23: 
           h = 0
           date +=1
           if date > int(Days_in_Month[month-1]):
                month += 1
                if month > 12:
                     year += 1
                     month = 1
                date = 1
       m = 15
   days -= 1
h = str(h)
m = str(m)
date = str(date)
month = str(month)
year = str(year)
f = open('time.txt','w')
f.write(date+"  "+month+"  "+year+"   "+h+"  "+m)
f.close()

ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

def read_ds_sensor():
    roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        msg = (temp)
        return (msg)
    return b'0.0'

print ('i here')
t4 = h+":"+m
ds = date+"/"+month+"/"+year
temp = read_ds_sensor()
temp1= (temp*10)
R1 = str(temp1)
R = ds+"-"+t4
g = open('r.txt','r')
l = g.read()
g.close()
x = float(l)
k = x + 0.2
g = open('r.txt','w')
g.write(str(k))
g.close()
M = str(k)
f2 = open('chart.html','a')
f2.write("<li class='data-point'onclick='S(this)'style='bottom:"+R1+"px; left:"+M+"px';"" data-type="" "+R+"-"+str(temp)+"C></li>"+'\n')
f2.close()
ft = open('table.html','a')
ft.write("<tr><td>"+R+"</td><td>"+temp+"</tr>"+'\n')
ft.close()

print ("finish")
time.sleep(2)