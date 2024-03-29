# GITHUB: @AbdelrhmanNile

import serial
import time
from rich import print
from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn
import pyttsx3
from speechs import *

def openSerial():
    global arduino
    arduino = serial.Serial('/dev/ttyACM0', 9600)

def main_func(): ## function  to read serial binary data from arduino
     # port changes based on your computer
    global arduino

    arduino_data = arduino.readline()

    #decode binary data to utf-8
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    values = decoded_values.split('x')
    #print("values: "+ values)
    # typecast the data to int
    for item in values:
        int_values.append(int(item))

    value = int_values[0]
    
    #reset values
    arduino_data = 0
    int_values.clear()
    values.clear()
    return value

def getBpm(): # function to get the BPM from main_func() 
    print("[red]\t\tPlease place your finger on the sensor and hold it still for 30 seconds\n")
    speech.say(finger_speech)
    speech.runAndWait()
    time.sleep(5)

    # progress bar
    text_column = TextColumn("[yellow]\tReading your BPM, please wait...", table_column=Column(ratio=1))
    bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
    progress = Progress(text_column, bar_column, expand=True)
    speech.say(wait_speech)
    speech.runAndWait()
    with progress:
        for n in progress.track(range(5)):
            time.sleep(0.1)
    
    # data will be read 4 times from the arduino to get the most accurate reading
    breaker = True
    i = 0
    while breaker:
        bpm = main_func()
        time.sleep(5)
        i = i + 1
        if(i == 3):
            breaker = False
            return bpm

    #bpm = main_func()
    #return bpm

# ----------------------------------------Main Code------------------------------------

# Declare variables to be used
values = []
int_values = []


