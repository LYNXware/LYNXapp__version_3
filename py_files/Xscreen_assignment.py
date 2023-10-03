print('Xscreen_assignment.py')

from kivy.uix.screenmanager import Screen
from kivy.properties import DictProperty
from kivy.uix.widget import Widget

from py_files.setup import setup


class AssignmentWindow(Screen):
    pass


class AssignmentWindowCustom(Widget):
    # current_button gets values from DeviceButton
    current_button = DictProperty({'name': '', 'function': '', 'description': ''})

    hexval_set = bytearray()
    function: str = ''

    def assign_event(self, key, hexval):
        self.hexval_set += hexval

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
        print('assignment.py -> save_button')
        name = self.current_button['name']

        if not self.hexval_set:
            self.ids.function.text = '* * * no assignment * * *'
        else:
            pass

        if name[0] == 'L':
            if setup.sublayer == 0:
                setup.main_left[name].ascii_set = self.hexval_set
                setup.main_left[name].function = self.function
                setup.main_left[name].description = self.ids.description.text
                print(f'assignment.py -> save_button main')
            else:
                setup.sub_left[name].ascii_set = self.hexval_set
                setup.sub_left[name].function = self.function
                setup.sub_left[name].description = self.ids.description.text
                print(f'assignment.py -> save_button sub')
        else:
            if setup.sublayer == 0:
                setup.main_right[name].ascii_set = self.hexval_set
                setup.main_right[name].function = self.function
                setup.main_right[name].description = self.ids.description.text
            else:
                setup.sub_right[name].ascii_set = self.hexval_set
                setup.sub_right[name].function = self.function
                setup.sub_right[name].description = self.ids.description.text

        setup.save_current_layout()
        print('assignment.py -> save_button -> setup.save_current_layout()')