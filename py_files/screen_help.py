from kivy.uix.screenmanager import ScreenManager, Screen
from __init__ import __version__
class HelpWindow(Screen):
    version = f'LYNX app - Version {__version__}'

    def open_link(self):
        import webbrowser
        webbrowser.open('https://www.lynx-workshop.com/')
