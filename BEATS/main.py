# GITHUB: @AbdelrhmanNile

from arduino import *
from beats import *
from functions import *
import os
os.system('clear')
engine = Bpm()
engine.reset()


welcome()

ready = int(Prompt.ask("[bold][red]Are you ready? [0 | 1]"))

if ready:
    fire_beats()
else:
    print("[yellow] Okay... \n Goodbye..")
    time.sleep(3)
    exit()

