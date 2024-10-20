from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test


age="7"
name=''
p1, p2, p3 = 0, 0, 0

a = 10
b = 11
a,b = b,a

c = b
b = a
a = c


#check

class InstScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = Label(text=txt_instruction)
        lbl1= Label(text='Введите имя:', halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2=  Label(text='Введите возраст:', halign='right')
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global name
        name = self.in_name.text
        #check old
        self.manager.current = 'pulse1'

class PulseScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = Label(text=txt_test1)
        lbl1= Label(text='Введите результат:', halign='right')
        self.pulse1 = TextInput(multiline=False)
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.pulse1)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p1
        p1 = int(self.pulse1.text)
        #check
        self.manager.current = 'sits'   

class CheckSits(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = Label(text=txt_sits)
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
            self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = Label(text=txt_test3)
        lbl1= Label(text='Результат:', halign='right')
        self.pulse2 = TextInput(multiline=False)
        lbl2=  Label(text='Результат после отдыха:', halign='right')
        self.pulse3 = TextInput(text='', multiline=False)
        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.pulse2)
        line2.add_widget(lbl2)
        line2.add_widget(self.pulse3)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p2, p3
        p2 = int(self.pulse2.text)
        p3 = int(self.pulse3.text)
        self.manager.current = 'result'

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation ='vertical', padding=8, spacing=8)
        self.instr = Label(text = '')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before
    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, int(age))

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm




app = HeartCheck()
app.run()