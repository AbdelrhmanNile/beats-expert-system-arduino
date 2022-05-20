# GITHUB: @AbdelrhmanNile

# main function
from arduino import *
from beats import *
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from time import sleep
from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn


engine = Bpm()
engine.reset()

print(Panel("[blue] Welcome to BEATS \n[red]-----------------------\n [cyan]BEATS is an Expert System \n that analyzes your healths based on your BPM \n [red]-----------------------\n [green]BEATS has a BPM sensor that will read your BPM \n  [yellow]BEATS only understands Binary values for Yes or No question \n  1 : Yes \n  0 : No", title="[red]BEATS", width=100, highlight=True))

ready = int(Prompt.ask("[bold][red]Are you ready? [0 | 1]"))
if ready:
    myage = int(Prompt.ask("[bold][blue]How old are you?"))
    mybpm = getBpm()
    print(Panel(f"[bold][cyan]your bpm is: {mybpm}", title="[red]BPM", width=25))

    engine.declare(Person(age=myage, bpm=mybpm))

    engine.run()
else:
    print("[yellow] Okay... \n Goodbye..")
    time.sleep(3)
    exit()

