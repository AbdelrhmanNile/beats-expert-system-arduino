# GITHUB: @AbdelrhmanNile
# BEATS Expert System

from experta import *
from rich import print
from rich.panel import Panel
from rich.layout import Layout
from speechs import *


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

    @Rule(AS.s << Person(smoke=W()))
    def smoking(self, s):
        if s['smoke'] == True:
            self.declare(Fact(is_smoker=True))
        else:
            self.declare(Fact(is_smoker=False))


    @Rule(AND(OR(Fact(is_athlete=L(True)), Fact(is_excellent=L(True)), Fact(is_great=L(True))), AS.s << Fact(is_smoker=W())))
    def very_healthy(self, s):
        self.declare(Fact(rate=10))
        if s['is_smoker'] == True:
            self.declare(Fact(is_new_smoker=True))
        else:
            self.declare(Fact(is_new_smoker=False))
    
    @Rule(AND(OR(Fact(is_good=L(True)), Fact(is_average=L(True)))))
    def healthy(self):
        self.declare(Fact(rate=7))

    @Rule(Fact(is_below_average=L(True)))
    def not_healthy(self):
        self.declare(Fact(rate=5))

    @Rule(Fact(is_poor=L(True)))
    def danger(self):
        self.declare(Fact(rate=2))


    @Rule(Fact(rate=L(10)), AS.s << Fact(is_new_smoker=W()))
    def nice(self, s):
        print(Panel("[green]Great job!\nYou are very healthy!\nKeep on working out an taking care of yourself!", title="[yellow]conclusion", width=35),end="55")
        speech.say(rate10_speech)
        speech.runAndWait()
        if s['is_new_smoker'] == True:
            print(Panel("[bold][red] you must be new to smoking\nit has not affect you health yet\n you need to stop smoking before it is to late", title="[red]WARNING", width=35))
            speech.say(new_smoker_speech)
            speech.runAndWait()

    @Rule(Fact(rate=L(7)))
    def okay(self):
        print(Panel("[green]Your health is Okay\nBut still it could be better\nYou might need to workout", title="[yellow]conclusion", width=35))
        speech.say(rate7_speech)
        speech.runAndWait()

    @Rule(Fact(rate=L(5)))
    def bleh(self):
        print(Panel("[yellow]Your health is below average\nYou need to watch your diet and workout", title="[yellow]conclusion", width=35))
        speech.say(rate5_speech)
        speech.runAndWait()

    @Rule(Fact(rate=L(2)))
    def very_bad(self):
        print(Panel("[red]Your health is very poor!!!!\nPlease visit a doctor ASAP to discuss your health issues", title="[yellow]conclusion", width=35))
        speech.say(rate2_speech)
        speech.runAndWait()

    @Rule(AND(OR(Fact(rate=L(7) | L(5))), Fact(is_smoker=L(True))))
    def _(self):
        print(Panel("[bold][red]Smoking has affected your health\nit will get worse if you did not stop",title="WARNING", width=35))
        speech.say(smoker_speech)
        speech.runAndWait()
