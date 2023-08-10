
import os
import pickle
import shutil

from plyer import filechooser

from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from py_files.events import left_events_dict, right_events_dict

from resource_path import resource_path
from py_files.user import user

from py_files import __version__

class LayoutsWindow(Screen):
    pass


class LayoutsWindowCustom(Widget):
    layer = StringProperty('major/minor')

    def select_layer(self):
        if self.layer == 'major/minor':
            self.layer = 'minor'
        elif self.layer == 'major':
            self.layer = 'minor'
        else:
            self.layer = 'major'

        self.ids.id_layoutSpinner.text = 'Existing Layouts'
        print(self.layer)

    def save_new_layout(self, layout_title):
        if self.layer == 'major/minor':
            self.ids.id_message_label.text = 'select layer: major or minor'
        elif not layout_title:
            self.ids.id_message_label.text = 'type in the layout title'
        else:
            with open(resource_path(f'user/layouts/{self.layer}/{layout_title}.pickle'), 'wb') as f:
                pickle.dump(left_events_dict, f)  # main_left - empty
                pickle.dump(right_events_dict, f)  # main_right - empty
                pickle.dump(left_events_dict, f)  # sub_left - empty
                pickle.dump(right_events_dict, f)  # sub_right - empty
                pickle.dump(__version__, f)
            self.ids.id_message_label.text = f'new layout "{layout_title}" was created'

    def find_layouts(self):
        if self.layer != 'major/minor':
            ll = os.listdir(resource_path(f'user/layouts/{self.layer}'))
            layouts_list = [x.split('.')[0] for x in ll]
            return layouts_list
        else:
            self.ids.id_message_label.text = 'select layer: major or minor'
            return []

    def copyLayout(self):
        layout = self.ids.id_layoutSpinner.text

        if layout == 'Existing Layouts':
            self.ids.id_message_label.text = 'Select Layout !!!'
        else:
            src = resource_path(f'user/layouts/{self.layer}/{layout}.pickle')
            dst = resource_path(f'user/layouts/{self.layer}/{layout}_copy.pickle')
            shutil.copyfile(src, dst)
            self.ids.id_message_label.text = f'Layout "{layout}" was copied.'

    def renameLayout(self):
        newTitle = self.ids.id_layout_title.text
        layout = self.ids.id_layoutSpinner.text

        if layout == 'Existing Layouts':
            self.ids.id_message_label.text = 'Select Layout'
        elif newTitle == '':
            self.ids.id_message_label.text = 'Type in new Layout Title !!!'
        else:
            src = resource_path(f'user/layouts/{self.layer}/{layout}.pickle')
            dst = resource_path(f'user/layouts/{self.layer}/{newTitle}.pickle')
            os.rename(src, dst)
            self.ids.id_message_label.text = f'Layout "{layout}" was renamed to "{newTitle}"'
            self.ids.id_layoutSpinner.text = newTitle

    def deleteLayout(self):

        layout = self.ids.id_layoutSpinner.text

        if layout == 'Existing Layouts':
            self.ids.id_message_label.text = 'Select Layout'

        elif len(os.listdir(resource_path(f'user/layouts/{self.layer}'))) <= 1:
            self.ids.id_message_label.text = f'{self.layer} folder must have at leased one layout.'

        else:
            src = resource_path(f'user/layouts/{self.layer}/{layout}.pickle')
            os.remove(src)
            self.ids.id_message_label.text = f'Layout "{layout}" was deleted.'
            self.ids.id_layoutSpinner.text = 'Existing Layouts'

            if layout == user.setup.selected_major_layout:
                ll = os.listdir(resource_path(f'user/layouts/major'))
                layouts_list = [x.split('.')[0] for x in ll]
                user.setup.update_major_layout(layouts_list[0])

            elif layout == user.setup.selected_minor_layout:
                print(user.setup.selected_minor_layout)
                ll = os.listdir(resource_path(f'user/layouts/minor'))
                layouts_list = [x.split('.')[0] for x in ll]
                user.setup.update_minor_layout(layouts_list[0])
                print(user.setup.selected_minor_layout)

    def import_layout(self):
        if self.layer == 'major/minor':
            self.ids.id_message_label.text = 'Select Layer: major or minor'
        else:
            import_directory = resource_path(f"user/layouts/{self.layer}")
            filters = ["*.pickle"]
            file_path = filechooser.open_file(filters=filters)[0]
            shutil.copy(file_path, import_directory)

    def export_layout(self):
        layout = self.ids.id_layoutSpinner.text
        if self.layer == 'major/minor':
            self.ids.id_message_label.text = 'Select Layer:  major or minor'
        elif layout == 'Existing Layouts':
            self.ids.id_message_label.text = 'Select Layout'
        else:
            file_path = resource_path(f"user/layouts/{self.layer}/{layout}.pickle")
            export_directory = filechooser.choose_dir()[0]
            shutil.copy(file_path, export_directory)

    def export_all(self):

        dest = f"{filechooser.choose_dir()[0]}/exported_layouts"
        print(dest)

        src = resource_path("user/layouts/")
        print(src)

        shutil.copytree(src, dest)

