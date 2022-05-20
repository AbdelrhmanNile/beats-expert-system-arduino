# GITHUB: @AbdelrhmanNile
# BEATS Expert System

from experta import *
from rich import print
from rich.panel import Panel

# class to hold Facts about the patient
# age and bpm
class Person(Fact):
    """info about the person"""
    pass

# Knowledge Engine
class Bpm(KnowledgeEngine):

    @Rule(Person(age=P(lambda x: 18 <= x <= 65)), Person(bpm = P(lambda y: 49 <= y <= 55)))
    def athlete(self):
        self.declare(Fact(is_athlete=True))

    @Rule(Person(age=P(lambda x: 18 <= x <= 65)), Person(bpm = P(lambda y: 56 <= y <= 61)))
    def excellenet(self):
        self.declare(Fact(is_excellent=True))

    @Rule(Person(age=P(lambda x: 18 <= x <= 65)), Person(bpm = P(lambda y: 62 <= y <= 65)))
    def great(self):
        self.declare(Fact(is_great=True))

    @Rule(Person(age=P(lambda x: 18 <= x <= 65)), Person(bpm = P(lambda y: 66 <= y <= 70)))
    def good(self):
        self.declare(Fact(is_good=True))

    @Rule(Person(age=P(lambda x: 18 <= x <= 65)), Person(bpm = P(lambda y: 70 <= y <= 75)))
    def average(self):
        self.declare(Fact(is_average=True))

    @Rule(Person(age=P(lambda x: 18 <= x <= 65)), Person(bpm = P(lambda y: 76 <= y <= 82)))
    def below_average(self):
        self.declare(Fact(is_below_average=True))

    @Rule(Person(age=P(lambda x: 18 <= x <= 65)), Person(bpm = P(lambda y: y >= 83)))
    def poor(self):
        self.declare(Fact(is_poor=True))


    @Rule(OR(Fact(is_athlete=L(True)), Fact(is_excellent=L(True)), Fact(is_great=L(True))))
    def very_healthy(self):
        self.declare(Fact(rate=10))
    
    @Rule(OR(Fact(is_good=L(True)), Fact(is_average=L(True))))
    def healthy(self):
        self.declare(Fact(rate=7))

    @Rule(Fact(is_below_average=L(True)))
    def not_healthy(self):
        self.declare(Fact(rate=5))

    @Rule(Fact(is_poor=L(True)))
    def danger(self):
        self.declare(Fact(rate=2))


    @Rule(Fact(rate=L(10)))
    def nice(self):
        print(Panel("[green]Great job!\nYou are very healthy!\nKeep on working out an taking care of yourself!", title="[yellow]conclusion", width=35))

    @Rule(Fact(rate=L(7)))
    def okay(self):
        print(Panel("[green]Your health is Okay\nBut still it could be better\nYou might need to workout", title="[yellow]conclusion", width=35))

    @Rule(Fact(rate=L(5)))
    def bleh(self):
        print(Panel("[yellow]Your health is below average\nYou need to watch your diet and workout", title="[yellow]conclusion", width=35))

    @Rule(Fact(rate=L(2)))
    def very_bad(self):
        print(Panel("[red]Your health is very poor!!!!\nPlease visit a doctor ASAP to discuss your health issues", title="[yellow]conclusion", width=35))


