"""
Version: 0.2.0
Date: 01.09.2023
Developer: Apd Devil
Remark:
"""

#dev 4.9.23

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from resource_path import resource_path


from py_files import __version__
print(f'LYNXapp Version: {__version__}')


from py_files.memory import create_memory_dir
# create a memory directory if it does not exist
create_memory_dir()

from py_files.theme import theme




# load pythong files for kivy CLASSES for the GUI
from py_files import screen_prime
from py_files import screen_assignment
from py_files import screen_layouts
from py_files import screen_theme
from py_files import screen_preferences
from py_files import screen_help
from py_files import custom_widgets

# load kivy files for the GUI
Builder.load_file(resource_path('kv_files/screen_prime.kv'))
Builder.load_file(resource_path('kv_files/screen_assignment.kv'))
Builder.load_file(resource_path('kv_files/modules.kv'))
Builder.load_file(resource_path('kv_files/screen_layouts.kv'))
Builder.load_file(resource_path('kv_files/screen_preferences.kv'))
Builder.load_file(resource_path('kv_files/screen_theme.kv'))
Builder.load_file(resource_path('kv_files/screen_help.kv'))
Builder.load_file(resource_path('kv_files/custom_widgets.kv'))



class KeyAssignment(Screen):
    pass



class WindowManager(ScreenManager):
    pass


class MainApp(App):

    KeyAssignmentScreenLoaded = False


    theme = DictProperty(theme.parameters)

    path_image_home = resource_path('images/home1.png')
    path_image_hands = resource_path('images/hands.png')


    def build(self):

        window_width = 1400
        window_height = 720
        screen_width = 1920
        screen_height = 1080

        Window.size = (window_width, window_height)
        Window.left = screen_width / 2 - window_width / 2
        Window.top = screen_height / 2 - window_height / 2

        main_kv = Builder.load_file(resource_path('kv_files/main.kv'))
        return main_kv

    def update_theme(self):
        self.theme = theme.parameters
        print('main.py -> update theme')

    def loadKeyAssignmentScreen(self):
        if not self.KeyAssignmentScreenLoaded:
            from py_files.screen_keyassignment import KeyAssignmentCustom
            Builder.load_file(resource_path('kv_files/screen_keyassignment.kv'))
            self.root.ids.keyassignment.add_widget(KeyAssignmentCustom())
            self.KeyAssignmentScreenLoaded = True
            print('test loaded')



if __name__ == '__main__':
    MainApp().run()


