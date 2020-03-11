from kivy.uix.widget import Widget
from kivy.app import App
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


class MyApp(App):
    def build(self):
        start = Widget()

        sign = ["RED", "GREEN", "YELLOW"]
        dropdown_traffic_sign = DropDownValues(sign)
        first_drop_down = Button(text='Sign', size_hint=(None, None), pos=(50, 450))
        first_drop_down.bind(on_release=dropdown_traffic_sign.dropDown.open)
        dropdown_traffic_sign.dropDown.bind(on_select=lambda instance, x: setattr(first_drop_down, 'text', x))

        speed = ["90","100","120","150","200","220"]
        dropdownCarSpeed = DropDownValues(speed)
        second_drop_down = Button(text="Speed", size_hint=(None, None), pos=(150, 450))
        second_drop_down.bind(on_release=dropdownCarSpeed.dropDown.open)
        dropdownCarSpeed.dropDown.bind(on_select=lambda instance, x: setattr(second_drop_down, 'text', x))

        location = ["Mohammadpur", "Dhanmondi", "Farmgate","Tangail"]
        dropdownCarLocation = DropDownValues(location)
        third_drop_down = Button(text='Location', size_hint=(None, None), pos=(250, 450))
        third_drop_down.bind(on_release=dropdownCarLocation.dropDown.open)
        dropdownCarLocation.dropDown.bind(on_select=lambda instance, x: setattr(third_drop_down, 'text', x))

        start.add_widget(first_drop_down)
        start.add_widget(second_drop_down)
        start.add_widget(third_drop_down)

        return start