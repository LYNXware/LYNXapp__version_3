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

        self.file_name = 'setup.json'

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

        # with open(resource_path(f'user/setup.pickle'), 'rb') as f:  # load last setup
        #     self.active_layer = pickle.load(f)  # mayor / minor
        #     self.sublayer = pickle.load(f)  # true / false
        #     self.selected_major_layout = pickle.load(f)
        #     self.selected_minor_layout = pickle.load(f)
        #     self.selected_device_left = pickle.load(f)
        #     self.selected_device_right = pickle.load(f)
        #
        #     if self.active_layer == 'major':
        #         self.active_layout = self.selected_major_layout
        #     else:
        #         self.active_layout = self.selected_minor_layout

    def save(self):
        save_data(self.data, self.file_name)

        # with open(resource_path(f'user/setup.pickle'), 'wb') as f:
        #     pickle.dump(self.active_layer, f)  # mayor / minor
        #     pickle.dump(self.sublayer, f)  # true / false
        #     pickle.dump(self.selected_major_layout, f)
        #     pickle.dump(self.selected_minor_layout, f)
        #     pickle.dump(self.selected_device_left, f)
        #     pickle.dump(self.selected_device_right, f)

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
# setup.save()0