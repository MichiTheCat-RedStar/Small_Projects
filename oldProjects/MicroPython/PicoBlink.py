from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
wait = 0

led.value(0)
while True:
    led.value(1)
    sleep(wait)
    led.value(0)
    sleep(wait)
    wait += 0.01
    print('Waiting Time:', round(wait, 2))