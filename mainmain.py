import machine, onewire, ds18x20, time import osfrom machine import Pinimport ESP8266WebServerled2 = Pin(14, Pin.OUT)led = Pin(5, Pin.OUT)def read_ds_sensor():      roms = ds_sensor.scan()      ds_sensor.convert_temp()      for rom in roms:          temp = ds_sensor.read_temp(rom)          msg = (temp)          return (msg)      return b'0.0'    f = open ('time.txt','r')fs=f.read()f.close()d = fs[:2]m = fs[2:4]y = fs[4:8]hs = fs[8:10]ms = fs[10:12]year = int(y)month = int(m)date = int(d)h = int(hs)m = int(ms)Days_in_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]days = 1while days > 0: m += 15 if m > 60:     h += 1     if h > 23:          h = 0         date +=1         if date > int(Days_in_Month[month-1]):              month += 1              if month > 12:                   year += 1                   month = 1              date = 1     m = 15 days -= 1if h < 10:  h = "0"+str(h)h = str(h)m = str(m)if date < 10:  date = "0"+str(date)date = str(date)if month < 10:  month = "0"+str(month)month = str(month)year = str(year)f = open('time.txt','w')f.write(date+month+year+h+m)f.close()    print ('i here')t4 = h+":"+mds = date+"/"+month+"/"+yeartemp = read_ds_sensor()temp1= (temp*10)R1 = str(temp1)R = ds+"-"+t4g = open('r.txt','r')l = g.read()g.close()x = float(l)k = x + 0.2g = open('r.txt','w')g.write(str(k))g.close()M = str(k)f2 = open('index.html','a')f2.write("<li class='data-point'onclick='S(this)'style='bottom:"+R1+"px; left:"+M+"px';"" data-type="" "+R+"-"+str(temp)+"C></li>"+'\n')f2.close()ft = open('table.html','a')ft.write("<tr><td>"+R+"</td><td>"+str(temp)+"</tr>"+'\n')ft.close()print ("finish")for i in range (5):  led.value(1)  time.sleep(0.1)  led.value(0)  time.sleep(0.1)machine.lightsleep (5000)#--------------------------------------------------------------------------------------ssid = 'VegeLogger'password = '123456789'ap = network.WLAN(network.AP_IF)ap.active(True)ap.config(essid=ssid,password=password)while ap.active() == False:  passprint('Connection successful')print(ap.ifconfig())    def index(socket, args):    ESP8266WebServer.ok(socket, "200", "index.html")def table(socket, args):    ESP8266WebServer.err(socket, "200", "table.html")ESP8266WebServer.begin(80)ESP8266WebServer.onPath("/index.html", index)ESP8266WebServer.onPath("localhost/table.html", table)ESP8266WebServer.onPath("localhost/chart.html", index)ESP8266WebServer.setDocPath("/")print("server start")for n in range (5):    led2.value(1)    time.sleep(0.1)    led2.value(0)    time.sleep(0.1)while True:    ESP8266WebServer.handleClient()