try:
  import usocket as socket
except:
  import socket


import network

import esp
esp.osdebug(None)

import gc
gc.collect()
wifi_set_sleep_type(LIGHT_SLEEP_T)
 