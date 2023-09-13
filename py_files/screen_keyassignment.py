
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import DictProperty

from py_files.ascii_language import asciiTable
from py_files.setup import setup



class CustomDynamicButton(Button):

    # def custom_callback(self):
    pass


class KeyAssignmentCustom(Widget):
    # current_button gets values from DeviceButton
    current_button = DictProperty({'name': '', 'function': '', 'description': ''})
    ascii_set = bytearray()
    function: str = ''


    def on_kv_post(self, *args):
        # print('KeyAssignmentCustom -> on_kv_post')
        # from py_files.ascii_language import asciiTable
        self.add_button(asciiTable.letters.items(), self.ids.letters)
        self.add_button(asciiTable.numbers.items(), self.ids.numbers)
        self.add_button(asciiTable.keypad1.items(), self.ids.keypad1)
        self.add_button(asciiTable.keypad2.items(), self.ids.keypad2)
        self.add_button(asciiTable.symbols.items(), self.ids.symbols)
        self.add_button(asciiTable.specials.items(), self.ids.specials)
        self.add_button(asciiTable.modifiers.items(), self.ids.modifiers)
        self.add_button(asciiTable.functions.items(), self.ids.functions)

    def add_button(self, ascii_dict, layout, ):
        for key, value in ascii_dict:
            custom_button = CustomDynamicButton(text=key)
            setattr(custom_button, 'asciiValue', bytes([value]))
            custom_button.bind(on_release=self.custom_callback)  # Bind the custom callback
            layout.add_widget(custom_button)


    def custom_callback(self, instance):
        print(f'callback {instance.text}  {instance.asciiValue}')
        self.assign_event(instance.text, instance.asciiValue)


    def assign_event(self, key, ascii_value):
        self.ascii_set += ascii_value
        # self.hexval_set += bytes([ascii_value])

        if self.function != '':
            self.function = f'{self.function} + {key}'
        else:
            self.function = key

        self.ids.function.text = self.function

        print(f'hexval_set: {self.ascii_set}  function: {self.function}')

    def reset(self):
        self.ascii_set = bytearray()
        self.function = ''
        self.ids.function.text = ''
        self.ids.description.text = ''

    def save_button(self):
        print('assignment.py -> save_button')
        name = self.current_button['name']

        if not self.ascii_set:
            self.ids.function.text = '* * * no assignment * * *'
        else:
            pass

        if name[0] == 'L':
            if setup.sublayer == 0:
                setup.main_left[name].ascii_set = self.ascii_set
                setup.main_left[name].function = self.function
                setup.main_left[name].description = self.ids.description.text
                print(f'assignment.py -> save_button main')
            else:
                setup.sub_left[name].ascii_set = self.ascii_set
                setup.sub_left[name].function = self.function
                setup.sub_left[name].description = self.ids.description.text
                print(f'assignment.py -> save_button sub')
        else:
            if setup.sublayer == 0:
                setup.main_right[name].ascii_set = self.ascii_set
                setup.main_right[name].function = self.function
                setup.main_right[name].description = self.ids.description.text
            else:
                setup.sub_right[name].ascii_set = self.ascii_set
                setup.sub_right[name].function = self.function
                setup.sub_right[name].description = self.ids.description.text

        setup.save_current_layout()
        print('assignment.py -> save_button -> setup.save_current_layout()')