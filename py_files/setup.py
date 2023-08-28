
from py_files.memory import load_data, save_data, load_layout, save_layout

from py_files.events import left_events_dict, right_events_dict
from py_files import __version__

print("setup.py")

class Setup():

    data = {}

    active_layer = 'major'
    sublayer = False
    active_layout = 'default'

    selected_major_layout = 'test_maojr'
    selected_minor_layout = 'test_minor'
    selected_device_left = 'CL-B00-B00-000'
    selected_device_right = 'CR-B00-BW0-M00'

    main_left = left_events_dict
    main_right = right_events_dict
    sub_left = left_events_dict
    sub_right = right_events_dict

    app_version = __version__

    def __init__(self):

        self.file_name = 'setup.pickle'

        self.swapping_button = None



        # self.data = {'active_layer': self.active_layer,
        #              'sublayer': self.sublayer,
        #              'selected_major_layout': self.selected_major_layout,
        #              'selected_minor_layout': self.selected_minor_layout,
        #              'selected_device_left': self.selected_device_left,
        #              'selected_device_right': self.selected_device_right,
        #              'main_left': self.main_left,
        #              'main_right': self.main_right,
        #              'sub_left': self.sub_left,
        #              'sub_right': self.sub_right,
        #              'app_version': self.app_version
        #              }



    def save(self):
        print(f'setup.py -> save: {self.active_layer}  {self.file_name}')

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

        self.data = load_data(self.file_name)

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



    def update_layout(self, file):
        print(f'setup.py -> load_layout: {self.active_layer}  {file}')

        self.data = load_layout(self.active_layer, file)

        self.main_left = self.data['main_left']
        self.main_right = self.data['main_right']
        self.sub_left = self.data['sub_left']
        self.sub_right = self.data['sub_right']

        self.app_version = self.data['app_version']

        self.save()



    def update_active_layer(self, x):
        print(f'setup.py -> update_active_layer: {x}')
        self.active_layer = x
        self.save()

    def update_sublayer(self, x):
        print(f'setup.py -> update_sublayer: {x}')
        self.sublayer = x
        self.save()

    def update_major_layout(self, x):
        print(f'setup.py -> update_major_layout: {x}')
        self.selected_major_layout = x
        self.active_layout = x
        self.save()

    def update_minor_layout(self, x):
        print(f'setup.py -> update_minor_layout: {x}')
        self.selected_minor_layout = x
        self.active_layout = x
        self.save()

    def update_device_left(self, x):
        print(f'setup.py -> update_device_left: {x}')
        self.selected_device_left = x
        self.save()

    def update_device_right(self, x):
        print(f'setup.py -> update_device_right: {x}')
        self.selected_device_right = x
        self.save()

    def event_swap(self, event_a, event_b):
        transit_a = None
        transit_b = None
        layout_a = None
        layout_b = None

        if self.sublayer:
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

        self.save_current_layout()
        self.save()


    def save_current_layout(self):
        print(f'setup.py -> save_current_layout: {self.active_layer}  {self.active_layout}')
        save_layout(self.active_layer,
                    self.active_layout,
                    self.main_left,
                    self.main_right,
                    self.sub_left,
                    self.sub_right,
                    self.app_version)



setup = Setup()
# setup.save()