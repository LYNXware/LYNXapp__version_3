
import os, sys
from kivy.resources import resource_add_path, resource_find

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


def resource_path(relative_path):
    # get absolute path to resource
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



Builder.load_file(resource_path('kvTest/login.kv'))
Builder.load_file(resource_path('kvTest/dashboard.kv'))
Builder.load_file(resource_path('kvTest/settings.kv'))





class LoginScreen(Screen):
    pass


class DashboardScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass

class MyMainApp(App):
    def build(self):
        return Builder.load_file(resource_path('kvTest/main.kv'))

if __name__ == '__main__':
    MyMainApp().run()
