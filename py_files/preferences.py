from py_files import __version__
from py_files.memory import load_data, save_data

print('preferences.py')

class Preferences:
    def __init__(self):
        self.file_name = 'preferences.pickle'
        self.parameters = load_data(self.file_name)
        # self.parameters = {
        #     'app_version': __version__,
        #     'key_display_name': True,
        #     'key_display_function': True,
        #     'key_display_description': True,
        #     'language_ascii': 'english'
        # }

    def load(self):
        load_data(self.file_name)


    def save(self):
        save_data(self.parameters, self.file_name)


    def get(self, key):
        return self.parameters.get(key)


    def set(self, key, value):
        if key in self.parameters:
            self.parameters[key] = value
            print(f'preferences.py -> set: {key} {value}')
            save_data(self.parameters, self.file_name)
        else:
            print(f"Invalid setting key: {key}")


# initialize preferences object
prefs = Preferences()
# prefs.save()
# print(f'-------------------------------------preferences.py -> prefs: {prefs.parameters}')
# # prefs.save()
