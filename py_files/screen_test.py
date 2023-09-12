
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from py_files.ascii_language import asciiTable



class CustomButton(Button):
    def custom_callback(self):
        pass


class TestCustom(Widget):
    def on_kv_post(self, *args):
        self.add_button(asciiTable.letters.items(), self.ids.letters)
        self.add_button(asciiTable.numbers.items(), self.ids.numbers)
        self.add_button(asciiTable.keypad.items(), self.ids.keypad)

    def add_button(self, ascii_dict, layout, ):
        for key, value in ascii_dict:
            custom_button = CustomButton(text=key)
            setattr(custom_button, 'asciiValue', value)
            custom_button.bind(on_release=self.custom_callback)  # Bind the custom callback
            layout.add_widget(custom_button)


    def custom_callback(self, instance):
        print(f'{instance.text}  {instance.asciiValue}')
        # self.addEve



