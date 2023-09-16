# Import the needed libraries
# random for RNG, time for sleep functionality, GPIO to get input from sensor
import random
import time
import RPi.GPIO as GPIO
from pygame import mixer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# The sensor is on GPIO pin 13
sensor = 13
GPIO.setup(sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
random.seed()
# set up sounds
mixer.init()
# codes 1 or 2
applause = mixer.Sound('audio/applause-1.wav')
# codes 3 or 4
boing = mixer.Sound('audio/boing.wav')
#codes 5 or 6
fart = mixer.Sound('audio/dramafart.wav')
# codes 7 or 8
f1 = mixer.Sound('audio/familyguytrans.wav')
# codes 9 or 10
f2 = mixer.Sound('audio/familyguytrans2.wav')
# codes 11 or 12
gasp = mixer.Sound('audio/gasp.wav')
# codes 13 or 14
hotdog = mixer.Sound('audio/hotdog.wav')
#codes 15 or 16
koth = mixer.Sound('audio/kingofthehill.wav')
#codes 17 or 18
laugh = mixer.Sound('audio/laugh.wav')
#codes 19 or 20
horns = mixer.Sound('audio/scaryhorns.wav')
#codes 21 or 22
s1 = mixer.Sound('audio/seinfeldlaugh.wav')
#codes 23 or 24
s2 = mixer.Sound('audio/seinfeldtrans.wav')

# confirms to user that program is initialized and running
startup = mixer.Sound('audio/wbong.wav')
startup.play()

def select(n):
    print(n)
    if n == 1 or n == 2:
        applause.play()
    if n == 3 or n == 4:
        boing.play()
    if n == 5 or n == 6:
        fart.play()
    if n == 7 or n == 8:
        f1.play()
    if n == 9 or n == 10:
        f2.play()
    if n == 11 or n == 12:
        gasp.play()
    if n == 13 or n == 14:
        hotdog.play()
    if n == 15 or n == 16:
        koth.play()
    if n == 17 or n == 18:
        laugh.play()
    if n == 19 or n == 20:
        horns.play()
    if n == 21 or n == 22:
        s1.play()
    if n == 23 or n == 24:
        s2.play()
    return


while True:
    if GPIO.input(sensor):
        number = random.randint(1, 24)
        print(number)
        select(number)
        while GPIO.input(sensor):
            time.sleep(5)
        time.sleep(5)
    else:
        print('I am too close!')
        time.sleep(5)
