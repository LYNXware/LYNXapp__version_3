

print("setup.py")
class Setup ():

    data = {}


    def __init__(self):
        print('setup.py -> __init__ ')

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