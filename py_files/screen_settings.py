from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from py_files.user import user
from py_files.preferences import prefs


class SettingsWindow(Screen):
    pass


class SettingsWindowCustom(Widget):
    def on_kv_post(self, *args):
        # self.ids.name.active = prefs.get('key_display_name')
        # self.ids.function.active = prefs.get('key_display_function')
        # self.ids.description.active = prefs.get('key_display_description')
        self.ids.name.active = user.preferences.button_name
        self.ids.function.active = user.preferences.button_function
        self.ids.description.active = user.preferences.button_description
        self.ids.float.add_widget(DeviceButton(pos_hint={'center_x': 0.75, 'center_y': 0.75}))
        self.update_button()

    def update_key_display(self, elements, state):
        prefs.set(elements, state)


    def update_name(self, state):
        user.preferences.update_b_name(state)
        self.update_button()
        # print(state)

    def update_function(self, state):
        user.preferences.update_b_function(state)
        self.update_button()
        # print(state)

    def update_description(self, state):
        user.preferences.update_b_description(state)
        self.update_button()
        # print(state)

    def update_button(self):
        self.ids.button_label.clear_widgets()

        if user.preferences.button_name:
            self.ids.button_label.add_widget(Label(text='Name',
                                                   color=user.theme.color_dict['button_name'],
                                                   font_size=15))
        if user.preferences.button_function:
            self.ids.button_label.add_widget(Label(text='Function',
                                                   color=user.theme.color_dict['button_function'],
                                                   font_size=15))
        if user.preferences.button_description:
            self.ids.button_label.add_widget(Label(text='Description',
                                                   color=user.theme.color_dict['button_description'],
                                                   font_size=15))
