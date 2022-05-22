# GITHUB: @AbdelrhmanNile
from speechs import *
from arduino import *
from beats import *
from functions import *
import os
from rich.layout import Layout
os.system('clear')
engine = Bpm()
engine.reset()

layout = Layout()

welcome()
speech.say(ready_speech)
speech.runAndWait()
ready = int(Prompt.ask("[bold][red]Are you ready? [0 | 1]"))
print()

if ready:
    fire_beats()
else:
    print("[yellow] Okay... \n Goodbye..")
    time.sleep(3)
    os.system('clear')
    exit()

