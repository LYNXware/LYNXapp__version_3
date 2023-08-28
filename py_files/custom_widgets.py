# from kivy.uix.actionbar import ActionBar
# from kivy.uix.spinner import Spinner
#
# class ActionBarCustom(ActionBar):
#     pass
#
# class GUI_Spinner(Spinner):
#     pass

from kivy.uix.button import Button
from kivy.uix.behaviors import DragBehavior
from kivy.properties import DictProperty
from kivy.uix.label import Label

from py_files.theme import theme
from py_files.preferences import prefs

from py_files.setup import setup


class DeviceButton(DragBehavior, Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme = DictProperty()
        self.theme = theme.parameters

        self.name = 'name'
        self.function = 'function'
        self.description = 'function'

        self.moving = False

    def on_kv_post(self, *args):

        if self.name[0] == 'L':
            if setup.sublayer == 0:
                self.function = setup.main_left[self.name].function
                self.description = setup.main_left[self.name].description
            else:
                self.function = setup.sub_left[self.name].function
                self.description = setup.sub_left[self.name].description
        elif self.name[0] == 'R':
            if setup.sublayer == 0:
                self.function = setup.main_right[self.name].function
                self.description = setup.main_right[self.name].description
            else:
                self.function = setup.sub_right[self.name].function
                self.description = setup.sub_right[self.name].description


        if prefs.get('key_display_name'):
            self.ids.button_label.add_widget(Label(text=self.name,
                                                   color=self.theme['button_name'],
                                                   font_size=self.fs))

        if prefs.get('key_display_function'):
            self.ids.button_label.add_widget(Label(text=self.function,
                                                   color=self.theme['button_function'],
                                                   font_size=self.fs))

        if prefs.get('key_display_description'):
            self.ids.button_label.add_widget(Label(text=self.description,
                                                   color=self.theme['button_description'],
                                                   font_size=self.fs))

    def on_pos(self, instance, value):
        if setup.swapping_button != self:
            setup.swapping_button = self