# Changes to original code on 2016-10-21 15:21 USA CT  
# Simplified blink() procedure for future enhancement  
# Moved threading references to main code section  
# Doubled sleep time (not significant)  
# Renamed "switch" to "flag_blinking" (not significant)  
# Introduced flag_exiting  

import tkinter as tk
import time
import threading

flag_blinking = False
flag_exiting = False

root = tk.Tk()


def blink():
    global flag_blinking
    global flag_exiting
    while (True):
        if (flag_blinking == True):
            print('BLINK...BLINK...')
        if (flag_exiting == True):
            return
        time.sleep(1.0)


def switchon():
    global flag_blinking
    flag_blinking = True
    print('flag_blinking on')


def switchoff():
    global flag_blinking
    flag_blinking = False
    print('flag_blinking off')


def kill():
    global flag_exiting
    flag_exiting = True
    root.destroy()


thread = threading.Thread(target=blink)
thread.start()

onbutton = tk.Button(root, text="Blink ON", command=switchon)
onbutton.pack()
offbutton = tk.Button(root, text="Blink OFF", command=switchoff)
offbutton.pack()
killbutton = tk.Button(root, text="EXIT", command=kill)
killbutton.pack()




def animate1(i):
    pullData = open('przemieszczenie.txt').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    a.clear()
    a.plot(xar,yar)
    return a
def animate2(i):
    pullData = open('predkosc.txt').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    b.clear()
    b.plot(xar,yar)
    return b
def animate3(i):
    pullData = open('przyspieszenie.txt').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    c1.clear()
    c1.plot(xar,yar)
    return c1