print('screen_help.py')

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from py_files import __version__

class HelpWindow(Screen):
    version = f'LYNX app - Version {__version__}'

    def open_link(self):
        import webbrowser
        webbrowser.open('https://www.lynx-workshop.com/')

class HelpWindowCustom(Widget):
    pass