
#testg

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import DictProperty, StringProperty


from py_files.functions import resource_path
from py_files.theme import theme




Builder.load_file(resource_path('kv_files/MainScreen.kv'))


Builder.load_file(resource_path('kv_files/custom_widgets.kv'))


class TestClass(Screen):
    pass



class MainScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class LYNXappApp(App):

    theme = DictProperty(theme.color_dict)
    path_image_home = resource_path('images/home1.png')
    path_image_hands = resource_path('images/hands.png')

    def build(self):
        return Builder.load_file(resource_path('kv_files/main.kv'))


if __name__ == '__main__':
    LYNXappApp().run()
