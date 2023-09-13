from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from py_files.theme import theme




class ThemeScreenCustom(Widget):

    def save_theme(self, element, color):
        theme.set(element, color)

    def bright_theme(self):
        theme.bright_theme()


    def dark_theme(self):
        theme.dark_theme()

