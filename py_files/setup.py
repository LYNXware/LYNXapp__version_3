from py_files.memory import load_data, save_data

from py_files.events import left_events_dict, right_events_dict
from py_files import __version__

print("setup.py")

class Setup():

    data = {}

    active_layer = 'major'
    sublayer = False
    active_layout = 'default'

    selected_major_layout = 'default'
    selected_minor_layout = 'default'
    selected_device_left = 'default'
    selected_device_right = 'default'

    main_left = left_events_dict
    main_right = right_events_dict
    sub_left = left_events_dict
    sub_right = right_events_dict

    app_version = __version__

    def __init__(self):

        self.file_name = 'setup.pickle'

        self.data = {'active_layer': self.active_layer,
                     'sublayer': self.sublayer,
                     'selected_major_layout': self.selected_major_layout,
                     'selected_minor_layout': self.selected_minor_layout,
                     'selected_device_left': self.selected_device_left,
                     'selected_device_right': self.selected_device_right,
                     'main_left': self.main_left,
                     'main_right': self.main_right,
                     'sub_left': self.sub_left,
                     'sub_right': self.sub_right,
                     'app_version': self.app_version
                     }



    def save(self):
        self.data['active_layer'] = self.active_layer
        self.data['sublayer'] = self.sublayer
        self.data['active_layout'] = self.active_layout

        self.data['selected_major_layout'] = self.selected_major_layout
        self.data['selected_minor_layout'] = self.selected_minor_layout
        self.data['selected_device_left'] = self.selected_device_left
        self.data['selected_device_right'] = self.selected_device_right

        self.data['main_left'] = self.main_left
        self.data['main_right'] = self.main_right
        self.data['sub_left'] = self.sub_left
        self.data['sub_right'] = self.sub_right

        self.data['app_version'] = self.app_version

        save_data(self.data, self.file_name)



    def load(self):
        self.active_layer = self.data['active_layer']
        self.sublayer = self.data['sublayer']
        self.active_layout = self.data['active_layout']

        self.selected_major_layout = self.data['selected_major_layout']
        self.selected_minor_layout = self.data['selected_minor_layout']
        self.selected_device_left = self.data['selected_device_left']
        self.selected_device_right = self.data['selected_device_right']

        self.main_left = self.data['main_left']
        self.main_right = self.data['main_right']
        self.sub_left = self.data['sub_left']
        self.sub_right = self.data['sub_right']

        self.app_version = self.data['app_version']

        load_data(self.file_name)




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


setup = Setup()
# setup.save()