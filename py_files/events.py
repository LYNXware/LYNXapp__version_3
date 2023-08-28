print('events.py started')


class EventClass:
    def __init__(self, ascii_set, function, description):
        self.ascii_set = ascii_set
        self.function = function
        self.description = description


events = [
    # finger buttons
    'I1',  # 0 array (c, r)
    'I2',  # 1
    'I3',  # 2
    'I4',  # 3
    'I5',  # 4
    'I6',  # 5
    'I7',  # 6

    'M1',  # 7
    'M2',  # 8
    'M3',  # 9
    'M4',  # 10

    'R1',  # 11
    'R2',  # 12
    'R3',  # 13
    'R4',  # 14

    'P1',  # 15
    'P2',  # 16
    'P3',  # 17
    'P4',  # 18
    'P5',  # 19

    # thumb buttons
    'TA1',  # 20
    'TA2',  # 21
    'TA3',  # 22
    'TA4',  # 23
    'TA5',  # 24

    'TB1',  # 25
    'TB2',  # 26
    'TB3',  # 27
    'TB4',  # 28
    'TB5',  # 29

    'TC3',  # 30

    # joystick
    'JM',  # 31
    'JS',  # 32

    'JF1',  # 33
    'JF2',  # 34

    'JB1',  # 35
    'JB2',  # 36

    'JL1',  # 37
    'JL2',  # 38

    'JR1',  # 39
    'JR2',  # 40

    # scroll wheel
    'WF',  # 41
    'WM',  # 42
    'WB',  # 43

    # mouse speed
    'MH',  # 44
    'MV'  # 45
]

left_events_dict = {}
right_events_dict = {}

events_main_left = {}
events_main_right = {}
events_sub_left = {}
events_sub_right = {}



for i, event in enumerate(events):
    # print(f'i {i}   b {event}')
    if event == 'MH' or event == 'MV':
        event_object_1 = EventClass(bytearray(b'\x64'), '-', '-')
        event_object_2 = EventClass(bytearray(b'\x65'), '-', '-')
        event_object_3 = EventClass(bytearray(b'\x66'), '-', '-')
        event_object_4 = EventClass(bytearray(b'\x67'), '-', '-')
    else:
        # event_object = EventClass(bytearray(b'\x30'), '-', '-')
        event_object_1 = EventClass(bytearray(b'\x31'), '-', '-')
        event_object_2 = EventClass(bytearray(b'\x32'), '-', '-')
        event_object_3 = EventClass(bytearray(b'\x33'), '-', '-')
        event_object_4 = EventClass(bytearray(b'\x34'), '-', '-')

    events_main_left[f'L{event}'] = event_object_1
    events_main_right[f'R{event}'] = event_object_2
    events_sub_left[f'L{event}'] = event_object_3
    events_sub_right[f'R{event}'] = event_object_4




print('events.py ended')
# print(left_events_dict)
# print(right_events_dict)
#
# print(right_events_dict['RI1'].ascii_set)
# print(right_events_dict['RMH'].ascii_set)
# print(right_events_dict['RMV'].ascii_set)
#
# print(left_events_dict['LI1'].ascii_set)
# print(left_events_dict['LMH'].ascii_set)
# print(left_events_dict['LMV'].ascii_set)
