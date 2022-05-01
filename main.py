from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import *
from kivy.metrics import *
from random import randint
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class pop(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app.ingame = 1
        self.all = BoxLayout(orientation='vertical')
        self.add_widget(self.all)

        self.lab = Label(text='Game is over your score is: '+str(app.timee))
        self.all.add_widget(self.lab)

        self.but = Button(text="exit")
        self.all.add_widget(self.but)
        self.but.bind(on_release=self.exitt)

    def exitt(self,b):
        exit()


class game(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bird = Image(source='bird.png',size_hint=(None,None),size=(dp(50),dp(50)),pos_hint={'x':app.birdx,'y':app.birdy})
        self.add_widget(self.bird)
        Clock.schedule_interval(self.grav, 0.001)
        Clock.schedule_interval(self.die, 0.09)
        Clock.schedule_interval(self.add, 2)

    def on_touch_down(self, touch):
        app.birdy += .07
        self.bird.pos_hint = {'x':app.birdx,'y':app.birdy}
    def grav(self,b):
        app.birdy -= 0.0013
        self.bird.pos_hint = {'x': app.birdx, 'y': app.birdy}
    def die(self,b):
        if app.birdy <= 0.03 or app.birdy >= 0.97:
            print("You are dead")
            Clock.schedule_once(self.op)
    def op(self,b):
        pop().open()

    def add(self,b):
        yyy = randint(50, 99)
        self.add_widget(bar(yy = (yyy-97)/100))
        self.add_widget(top_bar(yyy = yyy/100))


class bar(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0,1,0,1)
        self.size_hint = (.1,.5)
        self.pos_hint = {'x':self.xx,'y':self.yy}
        Clock.schedule_interval(self.come, .001)
        Clock.schedule_interval(self.bang, 0.01)

    def come(self,b):
        self.xx -= 0.004
        self.pos_hint = {'x': self.xx, 'y': self.yy}

    def bang(self,b):
        if self.xx-0.05<app.birdx<self.xx+0.05 and self.yy<app.birdy<self.yy+0.5:
            print("bang")
            pop().open()

    xx = NumericProperty(.9)
    yy = NumericProperty()

class top_bar(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0, 1, 0, 1)
        self.size_hint = (.1, .5)
        self.pos_hint = {'x': self.xxx, 'y': self.yyy}
        Clock.schedule_interval(self.come, .001)
        Clock.schedule_interval(self.bang_top, 0.01)

    def come(self,b):
        self.xxx -= 0.004
        self.pos_hint = {'x': self.xxx, 'y': self.yyy}

    def bang_top(self,b):
        if self.xxx - 0.05 < app.birdx < self.xxx + 0.05 and self.yyy < app.birdy < self.yyy+0.5:
            print("bang")
            pop().open()

    xxx = NumericProperty(.9)
    yyy = NumericProperty()

class app(App):
    def build(self):
        Clock.schedule_interval(self.plus, 1)
        return game()
    timee = NumericProperty(0)
    birdx = NumericProperty(.2)
    birdy = NumericProperty(.7)
    ingame = NumericProperty(0)
    def plus(self,b):
        if self.ingame == 0:
            self.timee += 1
        else:
            print("on menu")
if __name__ == "__main__":
    app = app()
    app.run()