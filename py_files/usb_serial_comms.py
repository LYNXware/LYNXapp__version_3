# this script is for usb port connection

import time
import threading
import serial.tools.list_ports


# class for serial communication with the cat via usb
class USB_cats:

    def __init__(self):
        self.ports_dict = {}
        self.lynxhub_port = ''
        self.available = 0
        self.right = []
        self.left = []
        self.running = False
        self.get_devices()

        self.monitoring_thread = threading.Thread(target=self.monitor_ports, args=(), daemon=True)
        self.monitoring_thread.start()

    # finds connected devices and sorts them into left and right
    def get_devices(self):

        self.running = True
        # print(f'usb_serial_comms.py -> running: {self.running}')
        self.ports_dict = {}
        self.right.clear()
        self.left.clear()


        ports_object = serial.tools.list_ports.comports()
        self.available = len(ports_object)
        print(f'usb_serial_comms.py -> available devices: {self.available}')



        for i in range(self.available):

            str_port = str(ports_object[i])
            # print(str_port)

            split_port = str_port.split(' ')
            comm_port = (split_port[0])

            serial_comm = serial.Serial(comm_port, baudrate=115200, timeout=1)
            serial_comm.write('are_you_a_cat'.encode())
            serial_comm.flush()

            time.sleep(0.1)

            response = serial_comm.readline().decode("utf-8")[:-2]
            serial_comm.close()
            print(f'usb_serial_comms.py -> response: {response}')

            if "LYNXhub" in response:
                self.add_lynxhub(comm_port, response)
            else:
                self.add_cats(comm_port, response)

        self.running = False
        print(f'usb_serial_comms.py -> running: {self.running}')


    def add_cats(self, port, response):

        self.ports_dict[response] = port

        if 'CL' in response:
            self.left.append(response)
        elif 'CR' in response:
            self.right.append(response)




    def add_lynxhub(self, port, response):
        self.lynxhub_port = port
        print(f'usb_serial_comms.py -> lynxhub_port: {self.lynxhub_port}')

        cats = response.split(':')

        for cat in cats:    # sort devices
            if 'CL' in cat:
                self.left.append(cat.split('_')[1])
            elif 'CR' in cat:
                self.right.append(cat.split('_')[1])



    # monitors usb ports for changes
    def monitor_ports(self):
        ports_count_old = len(serial.tools.list_ports.comports())
        print(f'usb_serial_comms.py -> monitor_ports')
        while True:
            time.sleep(0.5)
            ports_count = len(serial.tools.list_ports.comports())
            # print(f'ports count {ports_count}')
            if ports_count != ports_count_old:
                print(f'usb_serial_comms.py -> ports_count: {ports_count}')

                ports_count_old = ports_count
                self.get_devices()


devices = USB_cats()

print(devices.lynxhub_port)
print(devices.left)
print(devices.right)