import pickle

from py_files.functions import resource_path


class Theme:

    def __init__(self):
        with open(resource_path('pickle_files/theme.pickle'), 'rb') as f:
            self.color_dict = pickle.load(f)

    def save(self, widget_color, rgba):
        with open(resource_path('pickle_files/theme.pickle'), 'rb') as f:
            self.color_dict = pickle.load(f)
        self.color_dict[widget_color] = list(rgba)
        with open(resource_path('pickle_files/theme.pickle'), 'wb') as f:
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

        with open(resource_path('pickle_files/theme.pickle'), 'wb') as f:
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

        with open(resource_path('pickle_files/theme.pickle'), 'wb') as f:
            pickle.dump(self.color_dict, f)
        print('dark')


theme = Theme()
