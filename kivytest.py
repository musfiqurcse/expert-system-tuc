from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from core.button import CustomButton


class DropDownValues:
    def __init__(self, value):
        self.value = value
        self.dropDown = DropDown()
        if self.value.__len__() > 0:
            for index in range(self.value.__len__()):
                btn = Button(text= self.value[index], size_hint_y=None, height=50)
                btn.bind(on_release=lambda btn: self.dropDown.select(btn.text))
                self.dropDown.add_widget(btn)


class MyApp(App):
    def build(self):
        start = Widget(size = (500,500))
        self.title = 'Expert System TUC'
        Window.size = (500, 500)
        Window.set_title('Expert System TUC')
        layout = FloatLayout()
        sign = ["Vehicle", "Traffic", "Weather"]
        first_drop_down = CustomButton('Context',sign,50, 350)
        speed = ["90","100","120","150","200","220"]
        second_drop_down = CustomButton('Type',speed,150, 350)
        location = ["Mohammadpur", "Dhanmondi", "Farmgate", "Tangail"]
        third_drop_down = CustomButton('Value', location, 250, 350)
        # first_drop_down = Button(text='Context', font_size=12, size_hint=(None, None),size=(100,50), pos=(50, 350))
        # first_drop_down.bind(on_release=dropdown_traffic_sign.dropDown.open)
        # dropdown_traffic_sign.dropDown.bind(on_select=lambda instance, x: setattr(first_drop_down, 'text', x))

        # second_drop_down = Button(text="Type", size_hint=(None, None),size=(100,50), pos=(150, 350))
        # second_drop_down.bind(on_release=dropdownCarSpeed.dropDown.open)
        # dropdownCarSpeed.dropDown.bind(on_select=lambda instance, x: setattr(second_drop_down, 'text', x))


        # dropdownCarLocation = DropDownValues(location)
        # third_drop_down = Button(text='Value', size_hint=(None, None),size=(100,50), pos=(250, 350))
        # third_drop_down.bind(on_release=dropdownCarLocation.dropDown.open)
        # dropdownCarLocation.dropDown.bind(on_select=lambda instance, x: setattr(third_drop_down, 'text', x))

        start.add_widget(first_drop_down.return_current_button())
        start.add_widget(second_drop_down.return_current_button())
        start.add_widget(third_drop_down.return_current_button())

        return start


MyApp().run()
