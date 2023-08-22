import os
import shutil
from pathlib import Path
import json
# import pickle

from resource_path import resource_path

print("memory.py")


def get_memory_dir():
    # app_dir = Path(os.getcwd()).parent
    app_dir = os.getcwd()
    # print(f'memory -> get app_dir: {app_dir}')
    memory_dir = os.path.join(app_dir, "LYNXapp_Memory")
    print(f'memory.py -> get_memory_dir: {memory_dir}')
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






# Function to save data to a file
def save_data(data, file):

    memory_dir = get_memory_dir()
    filepath = os.path.join(memory_dir, file)
    print(f'memory.py -> save_data: {file}  {data}')

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


# Function to load data from a file
def load_data(file):

    memory_dir = get_memory_dir()
    filepath = os.path.join(memory_dir, file)
    print(f'memory.py -> load_data: {filepath}')

    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None



