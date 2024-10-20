from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        vl = BoxLayout(orientation='vertical', radding=8, spacing=8)
        hl = BoxLayout()
        txt = Label(text= 'Выбери экран')
        vl.add_widget(ScrButton(self, diraction='down', goal='first', text='1'))
        vl.add_widget(ScrButton(self, diraction='left', goal='second', text='2'))
        vl.add_widget(ScrButton(self, diraction='down', goal='first', text='3'))
        vl.add_widget(ScrButton(self, diraction='down', goal='first', text='4'))

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main'):
        super().__init__()
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.manager.transition.direction = self.direction
        self.manager.current = self.goal

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        btn = Button(text='Переключиться на следующий экран')
        btn.on.press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'left'

        self.manager.current = 'second'


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text='Переключиться на следующий экран')
        btn.on.press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        btn = Button(text='Переключиться на следующий экран')
        btn.on.press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'down'

        self.manager.current = 'four'

class FourthScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        btn = Button(text='Переключиться на следующий экран')
        btn.on.press = self.next
        self.add_widget(btn)

    #pass
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm
MyApp().run()
    