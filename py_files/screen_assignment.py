from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import DictProperty, StringProperty
from kivy.uix.widget import Widget

from user import user




class AssignmentWindow(Screen):
    pass


class AssignmentWindowCustom(Widget):
    # current_button gets values from DeviceButton
    current_button = DictProperty({'name': '', 'function': '', 'description': ''})

    hexval_set = bytearray()
    function: str = ''

    def assign_event(self, key, hexval):
        self.hexval_set += hexval

        print(self.hexval_set)

        if self.function != '':
            self.function = f'{self.function} + {key}'
        else:
            self.function = key
        self.ids.function.text = self.function

    def reset(self):
        self.hexval_set = bytearray()
        self.function = ''
        self.ids.function.text = ''
        self.ids.description.text = ''

    def save_button(self):
        name = self.current_button['name']

        if not self.hexval_set:
            self.ids.function.text = '* * * no assignment * * *'
        else:
            pass

        if name[0] == 'L':
            if user.setup.sublayer == 0:
                user.current_layout.main_left[name].ascii_set = self.hexval_set
                user.current_layout.main_left[name].function = self.function
                user.current_layout.main_left[name].description = self.ids.description.text
            else:
                user.current_layout.sub_left[name].ascii_set = self.hexval_set
                user.current_layout.sub_left[name].function = self.function
                user.current_layout.sub_left[name].description = self.ids.description.text
        else:
            if user.setup.sublayer == 0:
                user.current_layout.main_right[name].ascii_set = self.hexval_set
                user.current_layout.main_right[name].function = self.function
                user.current_layout.main_right[name].description = self.ids.description.text
            else:
                user.current_layout.sub_right[name].ascii_set = self.hexval_set
                user.current_layout.sub_right[name].function = self.function
                user.current_layout.sub_right[name].description = self.ids.description.text

        # layout.save(setup.current_layout)
        user.current_layout.save(user.setup.active_layout)
