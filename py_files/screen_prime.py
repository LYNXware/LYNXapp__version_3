
import os
import pickle

import serial.tools.list_ports

from kivy.clock import Clock
from kivy.properties import DictProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from py_files.usb_serial_comms import devices
from resource_path import resource_path
from py_files.user import user
from py_files.theme import theme

from py_files.preferences import prefs
from py_files.setup import setup


from py_files.memory import getLayouts, load_layout

class StartWindow(Screen):
    pass


class StartWindowCustom(Widget):
    # def on_touch_down(self, touch):
    #     print(touch)

    count_old = None
    # first_run = 0

    led_blue = (0, 0.3, 1, 1)
    led_green = (0, 1, 0, 1)
    led_red = (1, 0, 0, 1)
    led_off = (0, 0, 0, 0.3)

    def on_kv_post(self, *args):

        if setup.active_layer == 'major':
            self.ids.spinner_layouts.text = setup.selected_major_layout
            self.ids.id_major.led_color = self.led_blue
            self.ids.id_minor.led_color = self.led_off
            print(f'screen_prime.py active layer: {setup.active_layer}  selected layout: {setup.selected_major_layout}')
        else:
            self.ids.spinner_layouts.text = setup.selected_minor_layout
            self.ids.id_minor.led_color = self.led_green
            self.ids.id_major.led_color = self.led_off

        Clock.schedule_interval(self.window_clock_update, 1)

    def window_clock_update(self, *args):

        if devices.available != self.count_old:
            self.count_old = devices.available
            print(f'----------------------------------device count changed')

            while devices.running:
                print(f'devices.running {devices.running}')

            if not devices.left:
                setup.update_device_left('')
            else:
                setup.update_device_left(devices.left[0])

            if not devices.right:
                setup.update_device_right('')
            else:
                setup.update_device_right(devices.right[0])

            # print(f'devices:  {devices.left}  {devices.right}  - available {devices.available}')
            # print(
            #     f'user.devices  >{setup.selected_device_left}<   >{setup.selected_device_right}<  - count_old {self.count_old}')

            self.update_start_window()

    def update_start_window(self):
        self.ids.start_window.clear_widgets()

        if bool(setup.selected_device_left):
            # if True:
            # finger_modules = 'BW0'
            # thumb_modules = 'BJ0'
            # additional_modules = '000'
            thumb_modules = setup.selected_device_left[3:6]
            finger_modules = setup.selected_device_left[7:10]
            additional_modules = setup.selected_device_left[11:14]

            if 'B00' in thumb_modules:
                self.ids.start_window.add_widget(ThumbButtonsLeft())

            elif 'JB0' in thumb_modules:
                if setup.sublayer:
                    if setup.sub_left['LJS'].ascii_set == b'\x31':
                        self.ids.start_window.add_widget(JoystickLeft2())
                    else:
                        self.ids.start_window.add_widget(JoystickLeft())
                else:
                    if setup.main_left['LJS'].ascii_set == b'\x31':
                        self.ids.start_window.add_widget(JoystickLeft2())
                    else:
                        self.ids.start_window.add_widget(JoystickLeft())

            elif 'T00' in thumb_modules:
                # self.ids.start_window.add_widget(LeftThumbTrackball())
                pass
            else:
                pass

            if 'B00' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsLeft())
                self.ids.start_window.add_widget(FingerButtonsLeft2())

            elif 'BW0' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsLeft())
                self.ids.start_window.add_widget(WheelLeft())
            else:
                pass

            if 'M00' in additional_modules:
                self.ids.start_window.add_widget(MouseLeft())

        if bool(setup.selected_device_right):
            # if True:
            #     finger_modules = 'BW0'
            #     thumb_modules = 'BJ0'
            #     additional_modules = '000'

            thumb_modules = setup.selected_device_right[3:6]
            finger_modules = setup.selected_device_right[7:10]
            additional_modules = setup.selected_device_right[11:14]

            if 'B00' in thumb_modules:
                self.ids.start_window.add_widget(ThumbButtonsRight())
            elif 'JB0' in thumb_modules:
                if setup.sublayer:
                    if setup.sub_right['RJS'].ascii_set == b'\x31':
                        self.ids.start_window.add_widget(JoystickRight2())
                    else:
                        self.ids.start_window.add_widget(JoystickRight())
                else:
                    if setup.main_right['RJS'].ascii_set == b'\x31':
                        self.ids.start_window.add_widget(JoystickRight2())
                    else:
                        self.ids.start_window.add_widget(JoystickRight())
            if 'T00' in thumb_modules:
                # self.ids.start_window.add_widget(RightThumbTrackball())
                pass

            else:
                pass

            if 'B00' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsRight())
                self.ids.start_window.add_widget(FingerButtonsRight2())
            elif 'BW0' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsRight())
                self.ids.start_window.add_widget(WheelRight())
            else:
                pass

            if 'M00' in additional_modules:
                self.ids.start_window.add_widget(MouseRight())

        if len(devices.left) > 1:
            print('add left spinner')
            self.ids.start_window.add_widget(SpinnerLeft())
        if len(devices.right) > 1:
            print('add right spinner')
            self.ids.start_window.add_widget(SpinnerRight())

    def update_layout(self, new_layout):
        if setup.active_layer == 'major':
            setup.update_major_layout(new_layout)
            # setup.load(new_layout)
            setup.update_layout(new_layout)

        else:
            setup.update_minor_layout(new_layout)
            # setup.load(new_layout)
            setup.update_layout(new_layout)

    def get_layouts(self):  # get available layouts for the spinner
        if setup.active_layer == 'major':
            # ll = os.listdir(resource_path('user/layouts/major'))
            return getLayouts('major')
        else:
            # ll = os.listdir(resource_path('user/layouts/minor'))
            return getLayouts('minor')
        # print(ll)
        # layouts_list = [x.split('.')[0] for x in ll]
        # return layouts_list

    def select_layer(self):
        self.ids.id_sub.state = 'normal'
        setup.update_sublayer(False)
        # print(setup.sublayer)

        if setup.active_layer == 'major':
            setup.update_active_layer('minor')
            self.ids.id_minor.led_color = self.led_green
            self.ids.id_major.led_color = self.led_off
            self.ids.spinner_layouts.text = setup.selected_minor_layout
        else:
            setup.update_active_layer('major')
            self.ids.id_major.led_color = self.led_blue
            self.ids.id_minor.led_color = self.led_off
            self.ids.spinner_layouts.text = setup.selected_major_layout

    def select_sublayer(self, state):
        print(f'sublayer state: {state}')
        if state == 'down':
            setup.update_sublayer(True)
            if setup.active_layer == 'major':
                self.ids.id_major.led_color = self.led_red
            else:
                self.ids.id_minor.led_color = self.led_red
        else:
            setup.update_sublayer(False)
            if setup.active_layer == 'major':
                self.ids.id_major.led_color = self.led_blue
            else:
                self.ids.id_minor.led_color = self.led_green
        print(f'sublayer: {setup.sublayer}')
        # print(setup.sublayer)

    def transmit_layouts(self):

        # if self.first_run != 0:
        print(f'available devices for transmitting >{setup.selected_device_left}< >{setup.selected_device_right}<')

        if not setup.selected_device_left:
            print('no left device')
        else:
            comm_port = devices.ports_dict[setup.selected_device_left]
            print(comm_port)
            serial_comm = serial.Serial(comm_port, baudrate=115200, timeout=1)
            serial_comm.write(self.get_bytes('left'))
            serial_comm.flush()
            serial_comm.close()
            print('transmitted bytes left: ', self.get_bytes('left'))

        if not setup.selected_device_right:
            print('no right device')
        else:
            comm_port = devices.ports_dict[setup.selected_device_right]
            print(comm_port)
            serial_comm = serial.Serial(comm_port, baudrate=115200, timeout=1)
            serial_comm.write(self.get_bytes('right'))
            serial_comm.flush()
            serial_comm.close()
            print('transmitted bytes right: ', self.get_bytes('right'))

    def get_bytes(self, side):
        delimiter = bytearray(b'\xff')
        delimiter_layout = bytearray(b'\xfe')
        last_byte = b'\xfd'
        bytes_packet = bytearray(b'')
        b1 = None
        b2 = None
        b3 = None
        b4 = None

        # with open(resource_path(f'user/layouts/major/{setup.selected_major_layout}.pickle'), 'rb') as f:
        #     major_main_left = pickle.load(f)
        #     major_main_right = pickle.load(f)
        #     major_sub_left = pickle.load(f)
        #     major_sub_right = pickle.load(f)
        #
        # with open(resource_path(f'user/layouts/minor/{setup.selected_minor_layout}.pickle'), 'rb') as f:
        #     minor_main_left = pickle.load(f)
        #     minor_main_right = pickle.load(f)
        #     minor_sub_left = pickle.load(f)
        #     minor_sub_right = pickle.load(f)

        major_layout = load_layout('major', setup.selected_major_layout)
        major_main_left = major_layout['main_left']
        major_main_right = major_layout['main_right']
        major_sub_left = major_layout['sub_left']
        major_sub_right = major_layout['sub_right']

        minor_layout = load_layout('minor', setup.selected_minor_layout)
        minor_main_left = minor_layout['main_left']
        minor_main_right = minor_layout['main_right']
        minor_sub_left = minor_layout['sub_left']
        minor_sub_right = minor_layout['sub_right']


        if side == 'left':
            b1 = major_main_left
            b2 = major_sub_left
            b3 = minor_main_left
            b4 = minor_sub_left
        elif side == 'right':
            b1 = major_main_right
            b2 = major_sub_right
            b3 = minor_main_right
            b4 = minor_sub_right

        for b in b1.values():
            bytes_packet.extend(b.ascii_set)
            bytes_packet.extend(delimiter)
        bytes_packet.extend(delimiter_layout)

        for b in b2.values():
            bytes_packet.extend(b.ascii_set)
            bytes_packet.extend(delimiter)
        bytes_packet.extend(delimiter_layout)

        for b in b3.values():
            bytes_packet.extend(b.ascii_set)
            bytes_packet.extend(delimiter)
        bytes_packet.extend(delimiter_layout)

        for b in b4.values():
            bytes_packet.extend(b.ascii_set)
            bytes_packet.extend(delimiter)
        bytes_packet.extend(last_byte)

        return bytes_packet

    def check_button_collision(self):

        swap = False

        if not setup.swapping_button:
            pass
        else:
            if setup.swapping_button.moving:
                for module in self.ids.start_window.children:
                    for button in module.children[0].children:
                        if setup.swapping_button.collide_widget(button) and \
                                setup.swapping_button != button and \
                                type(setup.swapping_button) == type(button):
                            print(
                                f'collision: swapping_button {setup.swapping_button.name}  collision_button {button.name}')
                            setup.event_swap(setup.swapping_button.name, button.name)
                            swap = True

            setup.swapping_button.pos = setup.swapping_button.start_pos
            setup.swapping_button.moving = False

        if swap:
            self.update_start_window()
            swap = False


class SpinnerLeft(Widget):
    # spinner widget for devices if there is more than one
    def get_left_devices(self):
        return devices.left

    def change_device(self, device):
        setup.update_device_left(device)


class SpinnerRight(Widget):
    # spinner widget for devices if there is more than one
    def get_left_devices(self):
        return devices.right

    def change_device(self, device):
        setup.update_device_right(device)


class FingerButtonsLeft(Widget):
    pass


class FingerButtonsLeft2(Widget):
    pass


class FingerButtonsRight(Widget):
    pass


class FingerButtonsRight2(Widget):
    pass


class ThumbButtonsLeft(Widget):
    pass


class ThumbButtonsRight(Widget):
    pass


class JoystickLeft(Widget):
    def steps(self):
        if setup.sublayer and setup.sub_left['LJS'].ascii_set == b'\x30':
            setup.sub_left['LJS'].ascii_set = b'\x31'
        elif setup.sublayer and setup.sub_left['LJS'].ascii_set == b'\x31':
            setup.sub_left['LJS'].ascii_set = b'\x30'
        elif not setup.sublayer and setup.main_left['LJS'].ascii_set == b'\x30':
            setup.main_left['LJS'].ascii_set = b'\x31'
        elif not setup.sublayer and setup.main_left['LJS'].ascii_set == b'\x31':
            setup.main_left['LJS'].ascii_set = b'\x30'
        # setup.save(setup.active_layout)
        setup.save_current_layout()

class JoystickLeft2(Widget):
    def steps(self):
        if setup.sublayer and setup.sub_left['LJS'].ascii_set == b'\x30':
            setup.sub_left['LJS'].ascii_set = b'\x31'
        elif setup.sublayer and setup.sub_left['LJS'].ascii_set == b'\x31':
            setup.sub_left['LJS'].ascii_set = b'\x30'
        elif not setup.sublayer and setup.main_left['LJS'].ascii_set == b'\x30':
            setup.main_left['LJS'].ascii_set = b'\x31'
        elif not setup.sublayer and setup.main_left['LJS'].ascii_set == b'\x31':
            setup.main_left['LJS'].ascii_set = b'\x30'
        # setup.save(setup.active_layout)
        setup.save_current_layout()

class JoystickRight(Widget):
    def steps(self):
        if setup.sublayer and setup.sub_right['RJS'].ascii_set == b'\x30':
            setup.sub_right['RJS'].ascii_set = b'\x31'
        elif setup.sublayer and setup.sub_right['RJS'].ascii_set == b'\x31':
            setup.sub_right['RJS'].ascii_set = b'\x30'
        elif not setup.sublayer and setup.main_right['RJS'].ascii_set == b'\x30':
            setup.main_right['RJS'].ascii_set = b'\x31'
        elif not setup.sublayer and setup.main_right['RJS'].ascii_set == b'\x31':
            setup.main_right['RJS'].ascii_set = b'\x30'
        # setup.save(setup.active_layout)
        setup.save_current_layout()

class JoystickRight2(Widget):
    def steps(self):
        if setup.sublayer and setup.sub_right['RJS'].ascii_set == b'\x30':
            setup.sub_right['RJS'].ascii_set = b'\x31'
        elif setup.sublayer and setup.sub_right['RJS'].ascii_set == b'\x31':
            setup.sub_right['RJS'].ascii_set = b'\x30'
        elif not setup.sublayer and setup.main_right['RJS'].ascii_set == b'\x30':
            setup.main_right['RJS'].ascii_set = b'\x31'
        elif not setup.sublayer and setup.main_right['RJS'].ascii_set == b'\x31':
            setup.main_right['RJS'].ascii_set = b'\x30'
        # setup.save(setup.active_layout)
        setup.save_current_layout()

class WheelLeft(Widget):
    pass


class WheelRight(Widget):
    pass


class MouseLeft(Widget):
    def on_kv_post(self, *args):
        if setup.sublayer:
            h = ord(setup.sub_left['LMH'].ascii_set)
            v = ord(setup.sub_left['LMV'].ascii_set)
            self.ids.y_mouse_slider.value = v
            self.ids.x_mouse_slider.value = h
            self.ids.y_mouse_label.text = f'V = {v}'
            self.ids.x_mouse_label.text = f'H = {h}'
        else:
            h = ord(setup.main_left['LMH'].ascii_set)
            v = ord(setup.main_left['LMV'].ascii_set)
            self.ids.y_mouse_slider.value = v
            self.ids.x_mouse_slider.value = h
            self.ids.y_mouse_label.text = f'V = {v}'
            self.ids.x_mouse_label.text = f'H = {h}'

    def mouse_horizontal(self, x_factor):
        if setup.sublayer:
            setup.sub_left['LMH'].ascii_set = x_factor.to_bytes(1, byteorder='big')
            self.ids.x_mouse_label.text = f'H = {x_factor}'
        else:
            setup.main_left['LMH'].ascii_set = x_factor.to_bytes(1, byteorder='big')
            self.ids.x_mouse_label.text = f'H = {x_factor}'
        # setup.save(setup.active_layout)
        setup.save_current_layout()
    def mouse_vertical(self, y_factor):
        if setup.sublayer:
            setup.sub_left['LMV'].ascii_set = y_factor.to_bytes(1, byteorder='big')
            self.ids.y_mouse_label.text = f'V = {y_factor}'
        else:
            setup.main_left['LMV'].ascii_set = y_factor.to_bytes(1, byteorder='big')
            self.ids.y_mouse_label.text = f'V = {y_factor}'
        # setup.save(setup.active_layout)
        setup.save_current_layout()

class MouseRight(Widget):
    def on_kv_post(self, *args):
        if setup.sublayer:
            h = ord(setup.sub_right['RMH'].ascii_set)
            v = ord(setup.sub_right['RMV'].ascii_set)
            self.ids.y_mouse_slider.value = v
            self.ids.x_mouse_slider.value = h
            self.ids.y_mouse_label.text = f'V = {v}'
            self.ids.x_mouse_label.text = f'H = {h}'
        else:
            h = ord(setup.main_right['RMH'].ascii_set)
            v = ord(setup.main_right['RMV'].ascii_set)
            self.ids.y_mouse_slider.value = v
            self.ids.x_mouse_slider.value = h
            self.ids.y_mouse_label.text = f'V = {v}'
            self.ids.x_mouse_label.text = f'H = {h}'

    def mouse_horizontal(self, x_factor):
        if setup.sublayer:
            setup.sub_right['RMH'].ascii_set = x_factor.to_bytes(1, byteorder='big')
            self.ids.x_mouse_label.text = f'H = {x_factor}'
        else:
            setup.main_right['RMH'].ascii_set = x_factor.to_bytes(1, byteorder='big')
            self.ids.x_mouse_label.text = f'H = {x_factor}'
        # setup.save(setup.active_layout)
        setup.save_current_layout()

    def mouse_vertical(self, y_factor):
        if setup.sublayer:
            setup.sub_right['RMV'].ascii_set = y_factor.to_bytes(1, byteorder='big')
            self.ids.y_mouse_label.text = f'V = {y_factor}'
        else:
            setup.main_right['RMV'].ascii_set = y_factor.to_bytes(1, byteorder='big')
            self.ids.y_mouse_label.text = f'V = {y_factor}'
        # setup.save(setup.active_layout)
        setup.save_current_layout()


