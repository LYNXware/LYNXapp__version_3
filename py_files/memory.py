import os
import shutil
from pathlib import Path
# import json
import pickle

from resource_path import resource_path

print("memory.py")


def get_memory_dir():
    # app_dir = Path(os.getcwd()).parent
    app_dir = os.getcwd()
    # print(f'memory -> get app_dir: {app_dir}')
    memory_dir = os.path.join(app_dir, "LYNXapp_Memory")
    # print(f'memory.py -> get_memory_dir: {memory_dir}')
    return memory_dir


def create_memory_dir():
    print("memory.py -> create_memory_dir")

    memory_dir = get_memory_dir()

    if not os.path.exists(memory_dir):
        # print("memory.py -> create memory_dir")
        # os.makedirs(memory_dir)
        src_dir = resource_path('memory_embedded')
        shutil.copytree(src_dir, memory_dir)
        print("memory.py -> copytree")

    else:
        print("memory.py -> memory_dir exists")




def save_data(data, file):

    memory_dir = get_memory_dir()
    filepath = os.path.join(memory_dir, file)
    print(f'memory.py -> save_data: {file}  {data}')

    with open(filepath, 'wb') as f:
        pickle.dump(data, f)


# Function to load data from a file
def load_data(file):

    memory_dir = get_memory_dir()
    filepath = os.path.join(memory_dir, file)
    print(f'memory.py -> load_data: {filepath}')

    with open(filepath, 'rb') as f:
        return pickle.load(f)


def save_layout(layer, file, ml, mr, sl, sr, v):

    # data = {'main_left': left_events_dict,
    #         'main_right': right_events_dict,
    #         'sub_left': left_events_dict,
    #         'sub_right': right_events_dict,
    #         'app_version': __version__
    #         }

    data = {'main_left': ml,
            'main_right': mr,
            'sub_left': sl,
            'sub_right': sr,
            'app_version': v}

    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/layouts/{layer}/{file}.pickle'

    print(f'memory.py -> save_layouts: {filepath}')

    with open(filepath, 'wb') as f:
        pickle.dump(data, f)


def load_layout(layer, file):

    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/layouts/{layer}/{file}.pickle'

    print(f'memory.py -> load_layouts: {filepath}')

    with open(filepath, 'rb') as f:
        return pickle.load(f)


def getLayouts(layer):

    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/layouts/{layer}'

    layouts_list = os.listdir(filepath)
    layouts_list = [x.split('.')[0] for x in layouts_list]
    print(f'memory.py -> get_layouts: {layouts_list}')

    return layouts_list

    # def get_layout_data(layer, file):
    #
    #     memory_dir = get_memory_dir()
    #     filepath = f'{memory_dir}/layouts/{layer}/{file}.pickle'
    #
    #     print(f'memory.py -> get_layout_data: {filepath}')
    #
    #     with open(filepath, 'rb') as f:
    #         return pickle.load(f)



# Function to save data to a file
# def save_data(data, file):
#
#     memory_dir = get_memory_dir()
#     filepath = os.path.join(memory_dir, file)
#     print(f'memory.py -> save_data: {file}  {data}')
#
#     with open(filepath, 'w') as f:
#         json.dump(data, f, indent=4)
#
#
# # Function to load data from a file
# def load_data(file):
#
#     memory_dir = get_memory_dir()
#     filepath = os.path.join(memory_dir, file)
#     print(f'memory.py -> load_data: {filepath}')
#
#     try:
#         with open(filepath, 'r') as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return None



