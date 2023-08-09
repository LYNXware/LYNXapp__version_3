from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

from user import user

class ThemeWindow(Screen):
    pass


class ThemeWindowCustom(Widget):

    def test(self):
        print(user.theme.color_dict)

    def save_theme(self, widget_color, rgba):
        user.theme.save(widget_color, rgba)

    def bright_theme(self):
        user.theme.bright_theme()
        # print('bright)

    def dark_theme(self):
        user.theme.dark_theme()
        # print('update theme')
