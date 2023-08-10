
# this script creates a class to save all user data

import os
import pickle

# from pyautogui import size as screen_size
screen_size = (1920, 1080)


from resource_path import resource_path

from py_files import __version__



class Setup:
    def __init__(self):
        with open(resource_path(f'user/setup.pickle'), 'rb') as f:  # load last setup
            self.active_layer = pickle.load(f)              # mayor / minor
            self.sublayer = pickle.load(f)                  # true / false
            self.selected_major_layout = pickle.load(f)
            self.selected_minor_layout = pickle.load(f)
            self.selected_device_left = pickle.load(f)
            self.selected_device_right = pickle.load(f)

            if self.active_layer == 'major':
                self.active_layout = self.selected_major_layout
            else:
                self.active_layout = self.selected_minor_layout

    def update_active_layer(self, x):
        self.active_layer = x
        self.save()

    def update_sublayer(self, x):
        self.sublayer = x
        self.save()

    def update_major_layout(self, x):
        self.selected_major_layout = x
        self.active_layout = x
        self.save()

    def update_minor_layout(self, x):
        self.selected_minor_layout = x
        self.active_layout = x
        self.save()

    def update_device_left(self, x):
        self.selected_device_left = x
        self.save()

    def update_device_right(self, x):
        self.selected_device_right = x
        self.save()

    def save(self):
        with open(resource_path(f'user/setup.pickle'), 'wb') as f:
            pickle.dump(self.active_layer, f)  # mayor / minor
            pickle.dump(self.sublayer, f)  # true / false
            pickle.dump(self.selected_major_layout, f)
            pickle.dump(self.selected_minor_layout, f)
            pickle.dump(self.selected_device_left, f)
            pickle.dump(self.selected_device_right, f)


class CurrentLayout:
    # class that provides the information of the selected layout
    def __init__(self, setup):
        self.setup = setup

        self.main_left = None
        self.main_right = None
        self.sub_left = None
        self.sub_right = None

        self.app_version = None

        self.load(self.setup.active_layout)


    def save(self, layout_file):
        with open(resource_path(f'user/layouts/'
                                f'{self.setup.active_layer}/'
                                f'{layout_file}.pickle'), 'wb') as f:
            pickle.dump(self.main_left, f)
            pickle.dump(self.main_right, f)
            pickle.dump(self.sub_left, f)
            pickle.dump(self.sub_right, f)
            pickle.dump(__version__, f) # app_version

    def load(self, layout_file):
        ll = os.listdir(resource_path(f'user/layouts/{self.setup.active_layer}'))
        layouts_list = [x.split('.')[0] for x in ll]
        if layout_file not in layouts_list:
            layout_file = layouts_list[0]
        with open(resource_path(f'user/layouts/'
                                f'{self.setup.active_layer}/'
                                f'{layout_file}.pickle'), 'rb') as f:
            self.main_left = pickle.load(f)
            self.main_right = pickle.load(f)
            self.sub_left = pickle.load(f)
            self.sub_right = pickle.load(f)
            self.app_version = pickle.load(f) #'appVersion'

    def event_swap(self, event_a, event_b):
        transit_a = None
        transit_b = None
        layout_a = None
        layout_b = None

        if self.setup.sublayer:
            if event_a[0] == 'L':
                transit_a = self.sub_left[event_a]
                layout_a = self.sub_left
            elif event_a[0] == 'R':
                transit_a = self.sub_right[event_a]
                layout_a = self.sub_right
            if event_b[0] == 'L':
                transit_b = self.sub_left[event_b]
                layout_b = self.sub_left
            elif event_b[0] == 'R':
                transit_b = self.sub_right[event_b]
                layout_b = self.sub_right
        else:
            if event_a[0] == 'L':
                transit_a = self.main_left[event_a]
                layout_a = self.main_left
            elif event_a[0] == 'R':
                transit_a = self.main_right[event_a]
                layout_a = self.main_right
            if event_b[0] == 'L':
                transit_b = self.main_left[event_b]
                layout_b = self.main_left
            elif event_b[0] == 'R':
                transit_b = self.main_right[event_b]
                layout_b = self.main_right

        layout_a[event_a] = transit_b
        layout_b[event_b] = transit_a
        self.save(self.setup.active_layout)


class Preferences:

    def __init__(self):
        with open(resource_path(f'user/settings.pickle'), 'rb') as f:
            self.button_name = pickle.load(f)           # True/False
            self.button_function = pickle.load(f)       # True/False
            self.button_description = pickle.load(f)    # True/False

    def update_b_name(self, state):
        self.button_name = state
        self.save()

    def update_b_function(self, state):
        self.button_function = state
        self.save()

    def update_b_description(self, state):
        self.button_description = state
        self.save()

    def save(self):
        with open(resource_path(f'user/settings.pickle'), 'wb') as f:
            pickle.dump(self.button_name, f)
            pickle.dump(self.button_function, f)
            pickle.dump(self.button_description, f)


class Theme:

    def __init__(self):
        with open(resource_path('user/theme.pickle'), 'rb') as f:
            self.color_dict = pickle.load(f)


    def save(self, widget_color, rgba):
        with open(resource_path('user/theme.pickle'), 'rb') as f:
            self.color_dict = pickle.load(f)
        self.color_dict[widget_color] = list(rgba)
        with open(resource_path('user/theme.pickle'), 'wb') as f:
            pickle.dump(self.color_dict, f)



    def bright_theme(self):
        self.color_dict = {'background': [0.7254901960784313, 0.7254901960784313, 0.7254901960784313, 1],
                           'cat_button': [0.09999999999999998, 1, 0.841732283464567, 0.27121609798775154],
                           'button_name': [0.04391951006124248, 0.43919510061242345, 0.2909667541557306, 1],
                           'button_description': [0.10820209973753277, 0.05091863517060361, 0.5091863517060368, 1],
                           'cat_button_pushed': [0.9, 0, 0.15826771653543303, 1],
                           'button_function': [0.3132108486439195, 0.00191817667585961, 0.00191817667585961, 1],
                           'gui_text': [0.0, 0.0, 0.0, 1],
                           'gui_button': [0.0, 0.748300163266994, 0.7664041994750657, 0.3902012248468941],
                           'gui_button_pushed': [1.0, 0.251699836733006, 0.23359580052493434, 1],
                           'gui_dropdown': [0.0, 0.748300163266994, 0.7664041994750657, 1],
                           'gui_button_text': [0.0, 0.06865021137449676, 0.17672790901137359, 1]}


        with open(resource_path('user/theme.pickle'), 'wb') as f:
            pickle.dump(self.color_dict, f)
        print('bright')


    def dark_theme(self):
        self.color_dict = {'background': [0.20136852394916915, 0.20136852394916915, 0.20136852394916915, 1],
                           'cat_button': [0.09999999999999998, 0.6625, 1, 0.19941348973607037],
                           'button_name': [0.6, 0.7, 1, 1],
                           'button_description': [0.9375, 0.5, 1, 1],
                           'cat_button_pushed': [0.9, 0.3375, 0, 1],
                           'button_function': [0.09999999999999998, 1.0, 1, 1],
                           'gui_text': [1, 1, 1, 1],
                           'gui_button': [0.6, 0.85, 1, 0.4125122189638319],
                           'gui_button_pushed': [0.4, 0.15000000000000002, 0, 1],
                           'gui_dropdown': [0.6, 0.85, 1, 1],
                           'gui_button_text': [1, 1, 1, 1]}

        with open(resource_path('user/theme.pickle'), 'wb') as f:
            pickle.dump(self.color_dict, f)
        print('dark')



class User:
    def __init__(self):
        self.setup = Setup()
        self.current_layout = CurrentLayout(self.setup)
        self.preferences = Preferences()
        self.theme = Theme()

        self.swapping_button = None    # temporary variable for check_button_collision() in StartWindowCustom class

        self.screen_width, self.screen_height = screen_size


user = User()


print('------------------------user test')
print(user)
print(user.preferences)
print(user.preferences.button_name)

print(user.current_layout.main_left)

