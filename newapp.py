# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.core import text
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.bubble import Button

kivy.require('1.10.0') # replace with your current kivy version !

root = Builder.load_string(
'''
FloatLayout:
    canvas.before:
        Color:
            rgba:0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Button:
        text: '點選'
        font_name: 'kaiu.ttf'
        size_hint: .5, .5
        pos_hint:{'center_x':.5, 'center_y':.5}
'''
)

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = u'淡水Start Address'))
        self.s_startAddress = TextInput()
        self.add_widget(self.s_startAddress)

        self.add_widget(Label(text = 'End Address'))
        self.s_endAddress = TextInput()
        self.add_widget(self.s_endAddress)

        self.press = Button(text = 'Click me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print(self.s_startAddress.text)
        print(self.s_endAddress.text)

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()