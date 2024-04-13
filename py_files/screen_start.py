print("screen_start.py")

# import time
import serial.tools.list_ports

from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

from py_files.usb_serial_comms import devices
from py_files.setup import setup
from py_files.memory import getLayouts, load_layout

import py_files.constants as constants


# from py_files.constants import LEFT_CAT, RIGHT_CAT, DELIMITER_EVENT, DELIMITER_LAYOUT


class StartScreenCustom(FloatLayout):
    # def on_touch_down(self, touch):
    #     print(touch)
    count_old = None
    appStarted = False
    led_blue = (0, 0.3, 1, 1)
    led_green = (0, 1, 0, 1)
    led_red = (1, 0, 0, 1)
    led_off = (0, 0, 0, 0.3)

    def on_kv_post(self, *args):
        print('StartWindowCustom on_kv_post')
        self.appStarted = True

        if setup.selected_major_layout not in getLayouts('major'):
            setup.update_major_layout(getLayouts('major')[0])
        if setup.selected_minor_layout not in getLayouts('minor'):
            setup.update_minor_layout(getLayouts('minor')[0])

        if setup.active_layer == 'major':
            self.ids.spinner_layouts.text = setup.selected_major_layout
            if setup.sublayer:
                self.ids.id_sub.state = 'down'
                self.ids.id_major.led_color = self.led_red
                self.ids.id_minor.led_color = self.led_off
            else:
                self.ids.id_major.led_color = self.led_blue
                self.ids.id_minor.led_color = self.led_off
        else:
            self.ids.spinner_layouts.text = setup.selected_minor_layout
            if setup.sublayer:
                self.ids.id_sub.state = 'down'
                self.ids.id_minor.led_color = self.led_red
                self.ids.id_major.led_color = self.led_off
            else:
                self.ids.id_minor.led_color = self.led_green
                self.ids.id_major.led_color = self.led_off

        Clock.schedule_interval(self.window_clock_update, 1)
        self.appStarted = False

    def window_clock_update(self, *args):
        # print(f'screen_start.py -> window_clock_update')

        if devices.available != self.count_old:
            self.count_old = devices.available
            print(f'screen_start.py -> window_clock_update')

            # wait for serial thread to finish device search
            while devices.running:
                pass
                # print(f'screen_start.py -> devices.running {devices.running}')
                # import time
                # time.sleep(0.1)

            if not devices.left:
                setup.update_device_left('')
            else:
                setup.update_device_left(devices.left[0])

            if not devices.right:
                setup.update_device_right('')
            else:
                setup.update_device_right(devices.right[0])

            self.update_start_window()

    def update_start_window(self):
        print(f'screen_start.py -> update_start_window')
        self.ids.start_window.clear_widgets()

        if bool(setup.selected_device_left):
            thumb_modules = setup.selected_device_left[3:6]
            finger_modules = setup.selected_device_left[7:10]
            additional_modules = setup.selected_device_left[11:14]

            if 'K00' in thumb_modules:
                self.ids.start_window.add_widget(ThumbButtonsLeft())

            elif 'KJ0' in thumb_modules:
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


            if 'K00' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsLeft())
                self.ids.start_window.add_widget(FingerButtonsLeft2())
            elif 'KW0' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsLeft())
                self.ids.start_window.add_widget(WheelLeft())
            else:
                pass

            if 'M00' in additional_modules:
                self.ids.start_window.add_widget(MouseLeft())
            elif 'G00' in additional_modules:
                self.ids.start_window.add_widget(GyroscopeLeft())

        if bool(setup.selected_device_right):
            thumb_modules = setup.selected_device_right[3:6]
            finger_modules = setup.selected_device_right[7:10]
            additional_modules = setup.selected_device_right[11:14]

            if 'K00' in thumb_modules:
                self.ids.start_window.add_widget(ThumbButtonsRight())
            elif 'KJ0' in thumb_modules:
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

            if 'K00' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsRight())
                self.ids.start_window.add_widget(FingerButtonsRight2())
            elif 'KW0' in finger_modules:
                self.ids.start_window.add_widget(FingerButtonsRight())
                self.ids.start_window.add_widget(WheelRight())
            else:
                pass

            if 'M00' in additional_modules:
                self.ids.start_window.add_widget(MouseRight())
            elif 'G00' in additional_modules:
                self.ids.start_window.add_widget(GyroscopeRight())

        if len(devices.left) > 1:
            print('add left spinner')
            self.ids.start_window.add_widget(SpinnerLeft())
        if len(devices.right) > 1:
            print('add right spinner')
            self.ids.start_window.add_widget(SpinnerRight())


    def update_layout(self, new_layout):
        print(f'start_window_custom.py -> update_layout: {new_layout}')
        # prevent update on startup
        if not self.appStarted:
            if setup.active_layer == 'major':
                setup.update_major_layout(new_layout)
            else:
                setup.update_minor_layout(new_layout)

    def get_layouts(self):  # get available layouts for the spinner
        if setup.active_layer == 'major':
            return getLayouts('major')
        else:
            return getLayouts('minor')

    def select_layer(self):
        self.ids.id_sub.state = 'normal'
        setup.update_sublayer(False)

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
        print(f'screen_start.py -> select_sublayer: {state}')
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

    def transmit_layouts(self):

        # time.sleep(2)

        if not devices.lynxhub_port:
            self.transmit_layout_cats()
        else:
            self.transmit_layout_hub()

    def transmit_layout_hub(self):

        layouts_package = self.get_layouts_package()
        serial_comm = serial.Serial(devices.lynxhub_port, baudrate=115200, timeout=1)
        serial_comm.write(layouts_package)
        serial_comm.flush()
        serial_comm.close()


    def get_layouts_package(self):

        left_package = bytearray()
        right_package = bytearray()

        if bool(devices.left):
            left_package = self.packup_events('left')
        if bool(devices.right):
            right_package = self.packup_events('right')

        return left_package + right_package

    def packup_events(self, side):

        device_layouts_package = bytearray()

        if side == 'left':
            device_layouts_package = bytearray(constants.LEFT_CAT)
        elif side == 'right':
            device_layouts_package = bytearray(constants.RIGHT_CAT)

        major_layout = load_layout('major', setup.selected_major_layout)
        minor_layout = load_layout('minor', setup.selected_minor_layout)

        layouts = [major_layout['main_' + side],
                   major_layout['sub_' + side],
                   minor_layout['main_' + side],
                   minor_layout['sub_' + side]]

        for layout in layouts:
            for event in layout.values():
                device_layouts_package.extend(event.ascii_set)
                device_layouts_package.extend(constants.DELIMITER_EVENT)
            device_layouts_package.extend(constants.DELIMITER_LAYOUT)

        return device_layouts_package


    # def packup_events_cat(self, side):
    #
    #     device_layouts_package = bytearray()
    #
    #     major_layout = load_layout('major', setup.selected_major_layout)
    #     minor_layout = load_layout('minor', setup.selected_minor_layout)
    #
    #     layouts = [major_layout['main_' + side],
    #                major_layout['sub_' + side],
    #                minor_layout['main_' + side],
    #                minor_layout['sub_' + side]]
    #
    #     for layout in layouts:
    #         for event in layout.values():
    #             device_layouts_package.extend(event.ascii_set)
    #             device_layouts_package.extend(constants.DELIMITER_EVENT)
    #         device_layouts_package.extend(constants.DELIMITER_LAYOUT)
    #
    #     return device_layouts_package


    def transmit_layout_cats(self):

        print(f'connected >{setup.selected_device_left}< >{setup.selected_device_right}<')

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
        delimiter = constants.DELIMITER_EVENT #bytearray(b'\xff')
        delimiter_layout = constants.DELIMITER_LAYOUT # bytearray(b'\xfe')
        last_byte = b'\xfd'
        bytes_packet = bytearray(b'')
        b1 = None
        b2 = None
        b3 = None
        b4 = None

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
        print('JoystickLeft')
        print(setup.main_left['LJS'].ascii_set)


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
        print('------------------------------JoystickLeft2')


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

    def on_kv_post(self, *args):
        if setup.sublayer:
            ws = setup.sub_left['LWS'].ascii_set
        else:
            ws = setup.main_left['LWS'].ascii_set
        self.ids.left_ws.text = ws.decode('ascii')

    def set_wheel_speed(self, speed):
        s = speed.encode('ascii')
        if setup.sublayer:
            setup.sub_left['LWS'].ascii_set = s
        else:
            setup.main_left['LWS'].ascii_set = s
        setup.save_current_layout()


class WheelRight(Widget):

    def on_kv_post(self, *args):
        if setup.sublayer:
            ws = setup.sub_right['RWS'].ascii_set
        else:
            ws = setup.main_right['RWS'].ascii_set
        self.ids.right_ws.text = ws.decode('ascii')


    def set_wheel_speed(self, speed):
        s = speed.encode('ascii')
        if setup.sublayer:
            setup.sub_right['RWS'].ascii_set = s
        else:
            setup.main_right['RWS'].ascii_set = s
        setup.save_current_layout()


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

    def mouse_on(self):

        if setup.sublayer:
            setup.sub_left['LMNF'].ascii_set = b'\x31'
        else:
            setup.main_left['LMNF'].ascii_set = b'\x31'
        setup.save_current_layout()
        print('mouse on')

    def mouse_off(self):
        if setup.sublayer:
            setup.sub_left['LMNF'].ascii_set = b'\x30'
        else:
            setup.main_left['LMNF'].ascii_set = b'\x30'
        setup.save_current_layout()
        print('mouse off')




class MouseRight(Widget):
    def on_kv_post(self, *args):
        if setup.sublayer:
            h = ord(setup.sub_right['RMH'].ascii_set)
            v = ord(setup.sub_right['RMV'].ascii_set)
            self.ids.y_mouse_slider.value = v
            self.ids.x_mouse_slider.value = h
            self.ids.y_mouse_label.text = f'V = {v}'
            self.ids.x_mouse_label.text = f'H = {h}'

            if setup.sub_right['RMNF'].ascii_set == b'\x31':
                self.ids.mouse_right_toggle_on.state = 'down'
            else:
                self.ids.mouse_right_toggle_off.state = 'down'

        else:
            h = ord(setup.main_right['RMH'].ascii_set)
            v = ord(setup.main_right['RMV'].ascii_set)
            self.ids.y_mouse_slider.value = v
            self.ids.x_mouse_slider.value = h
            self.ids.y_mouse_label.text = f'V = {v}'
            self.ids.x_mouse_label.text = f'H = {h}'

            if setup.main_right['RMNF'].ascii_set == b'\x31':
                self.ids.mouse_right_toggle_on.state = 'down'
            else:
                self.ids.mouse_right_toggle_off.state = 'down'


    def mouse_horizontal(self, x_factor):
        if setup.sublayer:
            setup.sub_right['RMH'].ascii_set = x_factor.to_bytes(1, byteorder='big')
            self.ids.x_mouse_label.text = f'H = {x_factor}'
        else:
            setup.main_right['RMH'].ascii_set = x_factor.to_bytes(1, byteorder='big')
            self.ids.x_mouse_label.text = f'H = {x_factor}'
        setup.save_current_layout()

    def mouse_vertical(self, y_factor):
        if setup.sublayer:
            setup.sub_right['RMV'].ascii_set = y_factor.to_bytes(1, byteorder='big')
            self.ids.y_mouse_label.text = f'V = {y_factor}'
        else:
            setup.main_right['RMV'].ascii_set = y_factor.to_bytes(1, byteorder='big')
            self.ids.y_mouse_label.text = f'V = {y_factor}'
        setup.save_current_layout()

    def mouse_on(self):
        if setup.sublayer:
            setup.sub_right['RMNF'].ascii_set = b'\x31'
        else:
            setup.main_right['RMNF'].ascii_set = b'\x31'
        setup.save_current_layout()
        print('mouse on')

    def mouse_off(self):
        if setup.sublayer:
            setup.sub_right['RMNF'].ascii_set = b'\x30'
        else:
            setup.main_right['RMNF'].ascii_set = b'\x30'
        setup.save_current_layout()
        print('mouse off')


class GyroscopeLeft(Widget):

    def on_kv_post(self, *args):
        if setup.sublayer:
            if setup.sub_left['LGNF'].ascii_set == b'\x31':
                self.ids.gyro_left_on_off.text = 'ON'
            else:
                self.ids.gyro_left_on_off.text = 'OFF'

            if setup.sub_left['LGAR'].ascii_set == b'\x31':
                self.ids.gyro_left_absolute_relative.text = 'relativ'
            else:
                self.ids.gyro_left_absolute_relative.text = 'absolut'

            if setup.sub_left['LGM'].ascii_set == b'\x31':
                self.ids.gyro_left_mouse_on_off.text = 'M-ON'
            else:
                self.ids.gyro_left_mouse_on_off.text = 'M-OFF'

            if setup.sub_left['LGMXD'].ascii_set == b'\x30':
                self.ids.gyro_left_flip_x.text = 'X=0'
            else:
                self.ids.gyro_left_flip_x.text = 'X=180'

            if setup.sub_left['LGMYD'].ascii_set == b'\x30':
                self.ids.gyro_left_flip_y.text = 'Y=0'
            else:
                self.ids.gyro_left_flip_y.text = 'Y=180'

            self.ids.gyro_left_speed.text = setup.sub_left['LGMSF'].ascii_set.decode('ascii')
            self.ids.gyro_left_deadzone.text = setup.sub_left['LGDZ'].ascii_set.decode('ascii')


        else:
            if setup.main_left['LGNF'].ascii_set == b'\x31':
                self.ids.gyro_left_on_off.text = 'ON'
            else:
                self.ids.gyro_left_on_off.text = 'OFF'

            if setup.main_left['LGAR'].ascii_set == b'\x31':
                self.ids.gyro_left_absolute_relative.text = 'relativ'
            else:
                self.ids.gyro_left_absolute_relative.text = 'absolut'

            if setup.main_left['LGM'].ascii_set == b'\x31':
                self.ids.gyro_left_mouse_on_off.text = 'M-ON'
            else:
                self.ids.gyro_left_mouse_on_off.text = 'M-OFF'

            if setup.main_left['LGMXD'].ascii_set == b'\x30':
                self.ids.gyro_left_flip_x.text = 'X=0'
            else:
                self.ids.gyro_left_flip_x.text = 'X=180'

            if setup.main_left['LGMYD'].ascii_set == b'\x30':
                self.ids.gyro_left_flip_y.text = 'Y=0'
            else:
                self.ids.gyro_left_flip_y.text = 'Y=180'

            self.ids.gyro_left_speed.text = setup.main_left['LGMSF'].ascii_set.decode('ascii')
            self.ids.gyro_left_deadzone.text = setup.main_left['LGDZ'].ascii_set.decode('ascii')

    def gyro_on_off(self):
        gyro = ''
        if setup.sublayer and setup.sub_left['LGNF'].ascii_set == b'\x30':
            setup.sub_left['LGNF'].ascii_set = b'\x31'
            gyro = 'ON'
        elif setup.sublayer and setup.sub_left['LGNF'].ascii_set == b'\x31':
            setup.sub_left['LGNF'].ascii_set = b'\x30'
            gyro = 'OFF'
        elif not setup.sublayer and setup.main_left['LGNF'].ascii_set == b'\x30':
            setup.main_left['LGNF'].ascii_set = b'\x31'
            gyro = 'ON'
        elif not setup.sublayer and setup.main_left['LGNF'].ascii_set == b'\x31':
            setup.main_left['LGNF'].ascii_set = b'\x30'
            gyro = 'OFF'
        self.ids.gyro_left_on_off.text = gyro
        print(gyro)
        setup.save_current_layout()
        print(setup.main_left['LGNF'].ascii_set)

    def gyro_absolute_relative(self):
        gyro = ''
        if setup.sublayer and setup.sub_left['LGAR'].ascii_set == b'\x30':
            setup.sub_left['LGAR'].ascii_set = b'\x31'
            gyro = 'relativ'
        elif setup.sublayer and setup.sub_left['LGAR'].ascii_set == b'\x31':
            setup.sub_left['LGAR'].ascii_set = b'\x30'
            gyro = 'absolut'
        elif not setup.sublayer and setup.main_left['LGAR'].ascii_set == b'\x30':
            setup.main_left['LGAR'].ascii_set = b'\x31'
            gyro = 'relativ'
        elif not setup.sublayer and setup.main_left['LGAR'].ascii_set == b'\x31':
            setup.main_left['LGAR'].ascii_set = b'\x30'
            gyro = 'absolut'
        self.ids.gyro_left_absolute_relative.text = gyro
        print(gyro)
        setup.save_current_layout()
        print(setup.main_left['LGAR'].ascii_set)

    def gyro_mouse_on_off(self):
        gyro_mouse = ''
        if setup.sublayer and setup.sub_left['LGM'].ascii_set == b'\x30':
            setup.sub_left['LGM'].ascii_set = b'\x31'
            gyro_mouse = 'M-ON'
        elif setup.sublayer and setup.sub_left['LGM'].ascii_set == b'\x31':
            setup.sub_left['LGM'].ascii_set = b'\x30'
            gyro_mouse = 'M-OFF'
        elif not setup.sublayer and setup.main_left['LGM'].ascii_set == b'\x30':
            setup.main_left['LGM'].ascii_set = b'\x31'
            gyro_mouse = 'M-ON'
        elif not setup.sublayer and setup.main_left['LGM'].ascii_set == b'\x31':
            setup.main_left['LGM'].ascii_set = b'\x30'
            gyro_mouse = 'M-OFF'
        self.ids.gyro_left_mouse_on_off.text = gyro_mouse
        print(gyro_mouse)
        setup.save_current_layout()
        print(setup.main_left['LGNF'].ascii_set)

    def gyro_flip_x(self):
        gyro_flip_x = ''
        if setup.sublayer and setup.sub_left['LGMXD'].ascii_set == b'\x30':
            setup.sub_left['LGMXD'].ascii_set = b'\x31'
            gyro_flip_x = 'X=180'
        elif setup.sublayer and setup.sub_left['LGMXD'].ascii_set == b'\x31':
            setup.sub_left['LGMXD'].ascii_set = b'\x30'
            gyro_flip_x = 'X=0'
        elif not setup.sublayer and setup.main_left['LGMXD'].ascii_set == b'\x30':
            setup.main_left['LGMXD'].ascii_set = b'\x31'
            gyro_flip_x = 'X=180'
        elif not setup.sublayer and setup.main_left['LGMXD'].ascii_set == b'\x31':
            setup.main_left['LGMXD'].ascii_set = b'\x30'
            gyro_flip_x = 'X=0'
        self.ids.gyro_left_flip_x.text = gyro_flip_x
        setup.save_current_layout()

    def gyro_flip_y(self):
        gyro_flip_y = ''
        if setup.sublayer and setup.sub_left['LGMYD'].ascii_set == b'\x30':
            setup.sub_left['LGMYD'].ascii_set = b'\x31'
            gyro_flip_y = 'Y=180'
        elif setup.sublayer and setup.sub_left['LGMYD'].ascii_set == b'\x31':
            setup.sub_left['LGMYD'].ascii_set = b'\x30'
            gyro_flip_y = 'Y=0'
        elif not setup.sublayer and setup.main_left['LGMYD'].ascii_set == b'\x30':
            setup.main_left['LGMYD'].ascii_set = b'\x31'
            gyro_flip_y = 'Y=180'
        elif not setup.sublayer and setup.main_left['LGMYD'].ascii_set == b'\x31':
            setup.main_left['LGMYD'].ascii_set = b'\x30'
            gyro_flip_y = 'Y=0'
        self.ids.gyro_left_flip_y.text = gyro_flip_y
        setup.save_current_layout()

    def gyro_set_speed(self, speed):
        s = speed.encode('ascii')
        if setup.sublayer:
            setup.sub_left['LGMSF'].ascii_set = s
        else:
            setup.main_left['LGMSF'].ascii_set = s
        setup.save_current_layout()

    def gyro_set_deadzone(self, deadzone):
        d = deadzone.encode('ascii')
        if setup.sublayer:
            setup.sub_left['LGDZ'].ascii_set = d
        else:
            setup.main_left['LGDZ'].ascii_set = d
        setup.save_current_layout()


class GyroscopeRight(Widget):

        def on_kv_post(self, *args):
            if setup.sublayer:
                if setup.sub_right['RGNF'].ascii_set == b'\x31':
                    self.ids.gyro_right_on_off.text = 'ON'
                else:
                    self.ids.gyro_right_on_off.text = 'OFF'

                if setup.sub_right['RGAR'].ascii_set == b'\x31':
                    self.ids.gyro_right_absolute_relative.text = 'relativ'
                else:
                    self.ids.gyro_right_absolute_relative.text = 'absolut'

                if setup.sub_right['RGM'].ascii_set == b'\x31':
                    self.ids.gyro_right_mouse_on_off.text = 'M-ON'
                else:
                    self.ids.gyro_right_mouse_on_off.text = 'M-OFF'

                if setup.sub_right['RGMXD'].ascii_set == b'\x30':
                    self.ids.gyro_right_flip_x.text = 'X=0'
                else:
                    self.ids.gyro_right_flip_x.text = 'X=180'

                if setup.sub_right['RGMYD'].ascii_set == b'\x30':
                    self.ids.gyro_right_flip_y.text = 'Y=0'
                else:
                    self.ids.gyro_right_flip_y.text = 'Y=180'

                self.ids.gyro_right_speed.text = setup.sub_right['RGMSF'].ascii_set.decode('ascii')
                self.ids.gyro_right_deadzone.text = setup.sub_right['RGDZ'].ascii_set.decode('ascii')
            else:
                if setup.main_right['RGNF'].ascii_set == b'\x31':
                    self.ids.gyro_right_on_off.text = 'ON'
                else:
                    self.ids.gyro_right_on_off.text = 'OFF'

                if setup.main_right['RGAR'].ascii_set == b'\x31':
                    self.ids.gyro_right_absolute_relative.text = 'relativ'
                else:
                    self.ids.gyro_right_absolute_relative.text = 'absolut'

                if setup.main_right['RGM'].ascii_set == b'\x31':
                    self.ids.gyro_right_mouse_on_off.text = 'M-ON'
                else:
                    self.ids.gyro_right_mouse_on_off.text = 'M-OFF'

                if setup.main_right['RGMXD'].ascii_set == b'\x30':
                    self.ids.gyro_right_flip_x.text = 'X=0'
                else:
                    self.ids.gyro_right_flip_x.text = 'X=180'

                if setup.main_right['RGMYD'].ascii_set == b'\x30':
                    self.ids.gyro_right_flip_y.text = 'Y=0'
                else:
                    self.ids.gyro_right_flip_y.text = 'Y=180'

                self.ids.gyro_right_speed.text = setup.main_right['RGMSF'].ascii_set.decode('ascii')
                self.ids.gyro_right_deadzone.text = setup.main_right['RGDZ'].ascii_set.decode('ascii')

        def gyro_on_off(self):
            gyro = ''
            if setup.sublayer and setup.sub_right['RGNF'].ascii_set == b'\x30':
                setup.sub_right['RGNF'].ascii_set = b'\x31'
                gyro = 'ON'
            elif setup.sublayer and setup.sub_right['RGNF'].ascii_set == b'\x31':
                setup.sub_right['RGNF'].ascii_set = b'\x30'
                gyro = 'OFF'
            elif not setup.sublayer and setup.main_right['RGNF'].ascii_set == b'\x30':
                setup.main_right['RGNF'].ascii_set = b'\x31'
                gyro = 'ON'
            elif not setup.sublayer and setup.main_right['RGNF'].ascii_set == b'\x31':
                setup.main_right['RGNF'].ascii_set = b'\x30'
                gyro = 'OFF'
            self.ids.gyro_right_on_off.text = gyro
            setup.save_current_layout()

        def gyro_absolute_relative(self):
            gyro = ''
            if setup.sublayer and setup.sub_right['RGAR'].ascii_set == b'\x30':
                setup.sub_right['RGAR'].ascii_set = b'\x31'
                gyro = 'relativ'
            elif setup.sublayer and setup.sub_right['RGAR'].ascii_set == b'\x31':
                setup.sub_right['RGAR'].ascii_set = b'\x30'
                gyro = 'absolut'
            elif not setup.sublayer and setup.main_right['RGAR'].ascii_set == b'\x30':
                setup.main_right['RGAR'].ascii_set = b'\x31'
                gyro = 'relativ'
            elif not setup.sublayer and setup.main_right['RGAR'].ascii_set == b'\x31':
                setup.main_right['RGAR'].ascii_set = b'\x30'
                gyro = 'absolut'
            self.ids.gyro_right_absolute_relative.text = gyro
            setup.save_current_layout()

        def gyro_mouse_on_off(self):
            gyro_mouse = ''
            if setup.sublayer and setup.sub_right['RGM'].ascii_set == b'\x30':
                setup.sub_right['RGM'].ascii_set = b'\x31'
                gyro_mouse = 'M-ON'
            elif setup.sublayer and setup.sub_right['RGM'].ascii_set == b'\x31':
                setup.sub_right['RGM'].ascii_set = b'\x30'
                gyro_mouse = 'M-OFF'
            elif not setup.sublayer and setup.main_right['RGM'].ascii_set == b'\x30':
                setup.main_right['RGM'].ascii_set = b'\x31'
                gyro_mouse = 'M-ON'
            elif not setup.sublayer and setup.main_right['RGM'].ascii_set == b'\x31':
                setup.main_right['RGM'].ascii_set = b'\x30'
                gyro_mouse = 'M-OFF'
            self.ids.gyro_right_mouse_on_off.text = gyro_mouse
            setup.save_current_layout()

        def gyro_flip_x(self):
            gyro_flip_x = ''
            if setup.sublayer and setup.sub_right['RGMXD'].ascii_set == b'\x30':
                setup.sub_right['RGMXD'].ascii_set = b'\x31'
                gyro_flip_x = 'X=180'
            elif setup.sublayer and setup.sub_right['RGMXD'].ascii_set == b'\x31':
                setup.sub_right['RGMXD'].ascii_set = b'\x30'
                gyro_flip_x = 'X=0'
            elif not setup.sublayer and setup.main_right['RGMXD'].ascii_set == b'\x30':
                setup.main_right['RGMXD'].ascii_set = b'\x31'
                gyro_flip_x = 'X=180'
            elif not setup.sublayer and setup.main_right['RGMXD'].ascii_set == b'\x31':
                setup.main_right['RGMXD'].ascii_set = b'\x30'
                gyro_flip_x = 'X=0'
            self.ids.gyro_right_flip_x.text = gyro_flip_x
            setup.save_current_layout()

        def gyro_flip_y(self):
            gyro_flip_y = ''
            if setup.sublayer and setup.sub_right['RGMYD'].ascii_set == b'\x30':
                setup.sub_right['RGMYD'].ascii_set = b'\x31'
                gyro_flip_y = 'Y=180'
            elif setup.sublayer and setup.sub_right['RGMYD'].ascii_set == b'\x31':
                setup.sub_right['RGMYD'].ascii_set = b'\x30'
                gyro_flip_y = 'Y=0'
            elif not setup.sublayer and setup.main_right['RGMYD'].ascii_set == b'\x30':
                setup.main_right['RGMYD'].ascii_set = b'\x31'
                gyro_flip_y = 'Y=180'
            elif not setup.sublayer and setup.main_right['RGMYD'].ascii_set == b'\x31':
                setup.main_right['RGMYD'].ascii_set = b'\x30'
                gyro_flip_y = 'Y=0'
            self.ids.gyro_right_flip_y.text = gyro_flip_y
            setup.save_current_layout()

        def gyro_set_speed(self, speed):
            s = speed.encode('ascii')
            if setup.sublayer:
                setup.sub_right['RGMSF'].ascii_set = s
            else:
                setup.main_right['RGMSF'].ascii_set = s
            setup.save_current_layout()

        def gyro_set_deadzone(self, deadzone):
            d = deadzone.encode('ascii')
            if setup.sublayer:
                setup.sub_right['RGDZ'].ascii_set = d
            else:
                setup.main_right['RGDZ'].ascii_set = d
            setup.save_current_layout()
