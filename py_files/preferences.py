from py_files import __version__
from py_files.memory import load_data, save_data

print('preferences.py')

class Preferences:
    def __init__(self):

        self.file_name = 'preferences.json'

        # self.parameters = {
        #     'app_version': __version__,
        #     'key_display_name': True,
        #     'key_display_function': True,
        #     'key_display_description': True,
        #     'theme': 'light',
        # }

        # self.parameters = {}
        self.parameters = load_data(self.file_name)

        # self.current_settings = self.load()

    def load(self):
        load_data(self.file_name)

        # Simulate loading settings from a file or database
        # In a real implementation, you would read from a configuration file or database
        # return self.default_settings.copy()

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



# print(prefs.get('key_display_name'))
# prefs.set('key_display_name', False)
# print(prefs.get('key_display_name'))



# print(f'preferences.py -> prefs.parameters: {prefs.parameters}')
#
# print(f'preferences.py -> prefs.parameters: {prefs.parameters}')
# print(f'preferences.py -> prefs.get: {prefs.get("app_version")}')
# print(prefs.get('app_version'))
# print(prefs.parameters['app_version'])
# print(prefs)
# print(prefs.parameters)
# print(prefs.parameters['app_version'])




# Getting preferences
# theme = prefs.get('theme')
# font_size = prefs.get('font_size')
#
# print(f"Current theme: {theme}")
# print(f"Current font size: {font_size}")
#
# # Setting preferences
# prefs.set('font_size', 16)
# prefs.set('language', 'spanish')
