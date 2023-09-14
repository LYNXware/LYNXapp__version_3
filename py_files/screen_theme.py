from py_files.theme import theme
from kivy.uix.boxlayout import BoxLayout


class ThemeScreenCustom(BoxLayout):

    def save_theme(self, element, color):
        theme.set(element, color)

    def bright_theme(self):
        theme.bright_theme()


    def dark_theme(self):
        theme.dark_theme()

