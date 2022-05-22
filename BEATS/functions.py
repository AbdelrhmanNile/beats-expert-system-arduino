from beats import *
import arduino
from rich.prompt import Prompt
from time import sleep
from speechs import *


def welcome():
    print(Panel("[blue] Welcome to BEATS \n[red]-----------------------\n [cyan]BEATS is an Expert System \n that analyzes your health based on your BPM       \n [red]-----------------------\n [green]BEATS has a BPM sensor that will read your BPM \n  [yellow]BEATS only understands Binary values for Yes or No question \n  1 : Yes \n  0 : No", title="[red]BEATS", width=100, highlight=True))
    speech.say(welcoming_speech)
    speech.runAndWait()

def fire_beats():
    engine = Bpm()
    engine.reset()
    speech.say(age_speech)
    speech.runAndWait()
    myage = int(Prompt.ask("[bold][blue]How old are you?")); print()
    speech.say(smoke_speech)
    speech.runAndWait()
    smoker = int(Prompt.ask("[bold][cyan]Do you smoke? [0 | 1]")); print()
    try:
        mybpm = arduino.getBpm()
    except:
        print(Panel("[bold][red] ERROR: ARDUINO IS NOT CONNECTED", title="[bold][red]ERROR"))
        exit()
    
    print(Panel(f"[bold][cyan]your bpm is: {mybpm}", title="[red]BPM", width=35))
    speech.say(bpm_speech + str(mybpm))
    speech.runAndWait()

    engine.declare(Person(age=myage, bpm=mybpm, smoke=bool(smoker)))

    engine.run()
