from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

# from py_files.user import user

from py_files.theme import theme

class ThemeWindow(Screen):
    pass


class ThemeWindowCustom(Widget):

    def test(self):
        # print(user.theme.color_dict)
        print(f'theme.py -> test: {theme.parameters}')
    def save_theme(self, element, color):
        theme.set(element, color)
        # user.theme.save(element, color)

    def bright_theme(self):
        theme.bright_theme()
        # user.theme.bright_theme()
        # print('bright)

    def dark_theme(self):
        theme.dark_theme()
        # user.theme.dark_theme()
        # print('update theme')
