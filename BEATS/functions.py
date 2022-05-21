
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from time import sleep
from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn

def welcome():
    print(Panel("[blue] Welcome to BEATS \n[red]-----------------------\n [cyan]BEATS is an Expert System \n that analyzes your healths based on your BPM       \n [red]-----------------------\n [green]BEATS has a BPM sensor that will read your BPM \n  [yellow]BEATS only understands Binary values for Yes or No question \n  1 : Yes \n  0 : No", title="[red]BEATS", width=100, highlight=True))

def fire_beats():
    myage = int(Prompt.ask("[bold][blue]How old are you?"))
    smoker = int(Prompt.ask("[bold][cyan]Do you smoke? [0 | 1]"))
    try:
        mybpm = getBpm()
    except:
        print(Panel("[bold][red] ERROR: ARDUINO IS NOT CONNECTED", title="[bold][red]ERROR"))
        exit()
    
    print(Panel(f"[bold][cyan]your bpm is: {mybpm}", title="[red]BPM", width=25))

    engine.declare(Person(age=myage, bpm=mybpm, smoke=bool(smoker)))

    engine.run()
