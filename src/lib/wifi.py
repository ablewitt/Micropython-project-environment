
import network


def do_connect(essid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(essid, password)
        while not wlan.isconnected():
            pass
    print('Wifi client config:', wlan.ifconfig())

def test():
    pass

def start_ap(ap_name, pwd):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    print('creating AP:', ap_name)
    ap.config(essid=ap_name, password=pwd)
    print('Wifi AP details:', ap.ifconfig())
