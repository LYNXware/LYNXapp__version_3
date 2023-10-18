"""
Version: 0.2.0
Date: 01.09.2023
Developer: Apd Devil
Remark:
"""

# dev 18.09.23



from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from resource_path import resource_path
from py_files import __version__
from py_files.memory import create_memory_dir
# create a memory directory if it does not exist
create_memory_dir()
from py_files.theme import theme



class StartScreen(Screen):
    pass

class LayoutsScreen(Screen):
    pass


class ThemeScreen(Screen):
    pass


class PreferencesScreen(Screen):
    pass


class KeyAssignment(Screen):
    pass


class HelpScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(App):
    LayoutsScreenLoaded = False
    ThemeScreenLoaded = False
    PreferencesScreenLoaded = False
    KeyAssignmentScreenLoaded = False
    HelpScreenLoaded = False

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

        from py_files import screen_start
        from py_files import custom_widgets

        Builder.load_file(resource_path('kv_files/screen_start.kv'))
        Builder.load_file(resource_path('kv_files/modules.kv'))
        Builder.load_file(resource_path('kv_files/custom_widgets.kv'))

        main_kv = Builder.load_file(resource_path('kv_files/main.kv'))
        return main_kv

    def update_theme(self):
        self.theme = theme.parameters
        print('main.py -> update theme')

    def load_key_assignment_screen(self):
        if not self.KeyAssignmentScreenLoaded:
            from py_files.screen_keyassignment import KeyAssignmentCustom
            Builder.load_file(resource_path('kv_files/screen_keyassignment.kv'))
            self.root.ids.keyassignmentscreen.add_widget(KeyAssignmentCustom())
            self.KeyAssignmentScreenLoaded = True

    def load_layouts_screen(self):
        if not self.LayoutsScreenLoaded:
            from py_files.screen_layouts import LayoutsScreenCustom
            Builder.load_file(resource_path('kv_files/screen_layouts.kv'))
            self.root.ids.layoutsscreen.add_widget(LayoutsScreenCustom())
            self.LayoutsScreenLoaded = True

    def load_theme_screen(self):
        if not self.ThemeScreenLoaded:
            from py_files.screen_theme import ThemeScreenCustom
            Builder.load_file(resource_path('kv_files/screen_theme.kv'))
            self.root.ids.themescreen.add_widget(ThemeScreenCustom())
            self.ThemeScreenLoaded = True

    def load_preferences_screen(self):
        if not self.PreferencesScreenLoaded:
            from py_files.screen_preferences import PreferencesScreenCustom
            Builder.load_file(resource_path('kv_files/screen_preferences.kv'))
            self.root.ids.preferencesscreen.add_widget(PreferencesScreenCustom())
            self.PreferencesScreenLoaded = True

    def load_help_screen(self):
        if not self.HelpScreenLoaded:
            from py_files.screen_help import HelpScreenCustom
            Builder.load_file(resource_path('kv_files/screen_help.kv'))
            self.root.ids.helpscreen.add_widget(HelpScreenCustom())
            self.HelpScreenLoaded = True


if __name__ == '__main__':
    print(f'LYNXapp Version: {__version__}')
    MainApp().run()
