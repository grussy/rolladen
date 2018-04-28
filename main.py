import machine
import time

eins = machine.Pin(14, machine.Pin.OUT)
zwei = machine.Pin(27, machine.Pin.OUT)

def hoch():
    eins.value(1)
    zwei.value(0)
    time.sleep(35)
    zwei.value(1)
    

def runter():
    eins.value(0)
    zwei.value(1)
    time.sleep(35)
    eins.value(1)

def stop():
    eins.value(1)
    zwei.value(1)


stop()
