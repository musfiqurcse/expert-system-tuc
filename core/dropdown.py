
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class DropDownValues:
    def __init__(self, value):
        self.value = value
        self.dropDown = DropDown()
        if self.value.__len__() > 0:
            for index in range(self.value.__len__()):
                btn = Button(text= self.value[index], size_hint_y=None, height=50)
                btn.bind(on_release=lambda btn: self.dropDown.select(btn.text))
                self.dropDown.add_widget(btn)