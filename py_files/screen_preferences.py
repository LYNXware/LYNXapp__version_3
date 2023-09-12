print('screen_preferences.py')

from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from py_files.memory import getLanguages, loadLanguage
from py_files.preferences import prefs
from py_files.theme import theme


class SettingsWindow(Screen):
    pass


class SettingsWindowCustom(Widget):
    def on_kv_post(self, *args):
        self.ids.name.active = prefs.get('key_display_name')
        self.ids.function.active = prefs.get('key_display_function')
        self.ids.description.active = prefs.get('key_display_description')
        self.ids.spinner_language.text = prefs.get('language_ascii')
        self.update_button()

    def update_key_display(self, element, state):
        prefs.set(element, state)
        self.update_button()


    def update_button(self):
        self.ids.button_label.clear_widgets()

        # if user.preferences.button_name:
        if prefs.get('key_display_name'):
            self.ids.button_label.add_widget(Label(text='Name',
                                                   color=theme.get('button_name'),
                                                   font_size=15))
        # if user.preferences.button_function:
        if prefs.get('key_display_function'):
            self.ids.button_label.add_widget(Label(text='Function',
                                                   color=theme.get('button_function'),
                                                   font_size=15))
        # if user.preferences.button_description:
        if prefs.get('key_display_description'):
            self.ids.button_label.add_widget(Label(text='Description',
                                                   color=theme.get('button_description'),
                                                   font_size=15))

    def get_language(self):
        return getLanguages()

    def set_language(self, language):
        prefs.set('language_ascii', language)
        # self.ids.spinner_language.text = language
        # self.update_button()
        # self.update_language()