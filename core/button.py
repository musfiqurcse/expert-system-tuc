
from kivy.uix.button import Button
from core.dropdown import DropDownValues

class CustomButton():

    def __init__(self,label: str, value: list, posX : int , posY : int ):
        self.sign = value
        self.dropDown = DropDownValues(self.sign);
        self.button = Button(text=label, font_size=12, size_hint=(None, None), size=(100, 50), pos=(posX, posY))
        self.button.bind(on_release=self.dropDown.dropDown.open)
        self.dropDown.dropDown.bind(on_select=lambda instance, x: setattr( self.button, 'text', x))


    def return_current_button(self):
        return  self.button