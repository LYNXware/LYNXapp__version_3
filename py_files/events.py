print('events.py started')


class EventClass:
    def __init__(self, ascii_set, function, description):
        self.ascii_set = ascii_set
        self.function = function
        self.description = description


events = [
    # index finger events
    'I1',  # 0
    'I2',  # 1
    'I3',  # 2
    'I4',  # 3
    'I5',  # 4
    'I6',  # 5
    'I7',  # 6
    # middle finger events
    'M1',  # 7
    'M2',  # 8
    'M3',  # 9
    'M4',  # 10
    # ring finger events
    'R1',  # 11
    'R2',  # 12
    'R3',  # 13
    'R4',  # 14
    # pinky finger events
    'P1',  # 15
    'P2',  # 16
    'P3',  # 17
    'P4',  # 18
    'P5',  # 19

    # thumb events
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

    # joystick events
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

    # scroll wheel events
    'WM',  # 41
    'WF',  # 42
    'WB',  # 43
    'WS',  # 44

    # mouse
    'MNF',  # 45 on/off
    'MH',  # 46
    'MV',  # 47

    # gyroscope
    'GNF',  # 48 on/off
    'GAR',   # 49 absolute/relative
    'GM',   # 50 with mouse
    'GMSF',  # 51 mouse speed factor
    'GMXD',  # 52 mouse x direction
    'GMYD',  # 53 mouse y direction
    'GF',    # 54 forward
    'GB',   # 55 backward
    'GL',   # 56 left
    'GR',   # 57 right
]


events_main_left = {}
events_main_right = {}
events_sub_left = {}
events_sub_right = {}


for i, event in enumerate(events):
    # print(f'i {i}   b {event}')
    if event == 'MH' or event == 'MV':
        event_object_1 = EventClass(bytearray(b'\x64'), '-', '-') # 100
        event_object_2 = EventClass(bytearray(b'\x64'), '-', '-') # 100
        event_object_3 = EventClass(bytearray(b'\x64'), '-', '-') # 100
        event_object_4 = EventClass(bytearray(b'\x64'), '-', '-') # 100
    elif event == 'GNF' or event == 'GM' or event == 'GAR':
        event_object_1 = EventClass(bytearray(b'\x30'), '0', '0') # 0 flag off
        event_object_2 = EventClass(bytearray(b'\x30'), '0', '0') # 0 flag off
        event_object_3 = EventClass(bytearray(b'\x30'), '0', '0') # 0 flag off
        event_object_4 = EventClass(bytearray(b'\x30'), '0', '0') # 0 flag off
    else:
        # event_object = EventClass(bytearray(b'\x30'), '-', '-')
        # event_object_1 = EventClass(bytearray(b'\x30'), '0', '0')
        # event_object_2 = EventClass(bytearray(b'\x30'), '0', '0')
        # event_object_3 = EventClass(bytearray(b'\x30'), '0', '0')
        # event_object_4 = EventClass(bytearray(b'\x30'), '0', '0')
        event_object_1 = EventClass(bytearray(b'\x1a\xf0'), 'none', 'none')
        event_object_2 = EventClass(bytearray(b'\x1a\xf0'), 'none', 'none')
        event_object_3 = EventClass(bytearray(b'\x1a\xf0'), 'none', 'none')
        event_object_4 = EventClass(bytearray(b'\x1a\xf0'), 'none', 'none')
    events_main_left[f'L{event}'] = event_object_1
    events_main_right[f'R{event}'] = event_object_2
    events_sub_left[f'L{event}'] = event_object_3
    events_sub_right[f'R{event}'] = event_object_4



print('events.py ended')

