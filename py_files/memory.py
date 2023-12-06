import os
import shutil
import pickle
import json

from resource_path import resource_path

print("memory.py")


def get_memory_dir():
    app_dir = os.getcwd()
    memory_dir = os.path.join(app_dir, "LYNXapp_Memory")
    return memory_dir


def create_memory_dir():
    memory_dir = get_memory_dir()
    if not os.path.exists(memory_dir):
        src_dir = resource_path('memory_embedded')
        shutil.copytree(src_dir, memory_dir)
        print("memory.py -> copytree")
    else:
        print("memory.py -> memory_dir exists")




def save_data(data, file):
    print(f'memory.py -> save_data: {file}  {data}')
    memory_dir = get_memory_dir()
    filepath = os.path.join(memory_dir, file)
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)


# Function to load data from a file
def load_data(file):
    print(f'memory.py -> load_data: {file}')
    memory_dir = get_memory_dir()
    filepath = os.path.join(memory_dir, file)
    with open(filepath, 'rb') as f:
        return pickle.load(f)


def save_layout(layer, file, ml, mr, sl, sr, v):
    print(f'memory.py -> save_layouts: {file}')
    data = {'main_left': ml,
            'main_right': mr,
            'sub_left': sl,
            'sub_right': sr,
            'app_version': v}
    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/layouts/{layer}/{file}.pickle'
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)


def load_layout(layer, file):
    print(f'memory.py -> load_layouts: {file}')
    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/layouts/{layer}/{file}.pickle'

    if not os.path.exists(filepath):
        print(os.listdir(f'{memory_dir}/layouts/{layer}'))
        filepath = f'{memory_dir}/layouts/{layer}/{os.listdir(f"{memory_dir}/layouts/{layer}")[0]}'

    with open(filepath, 'rb') as f:
        return pickle.load(f)


def getLayouts(layer):
    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/layouts/{layer}'
    layouts_list = os.listdir(filepath)
    layouts_list = [x.split('.')[0] for x in layouts_list]
    print(f'memory.py -> get_layouts: {layouts_list}')
    return layouts_list


def getAsciiLanguages():
    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/KeyTable_Language'
    languages_list = os.listdir(filepath)
    languages_list = [x.split('.')[0] for x in languages_list]
    print(f'memory.py -> get_languages: {languages_list}')
    return languages_list

def loadAsciiLanguage(language):
    memory_dir = get_memory_dir()
    filepath = f'{memory_dir}/KeyTable_Language/{language}.json'

    if not os.path.exists(filepath):
        filepath = f'{memory_dir}/KeyTable_Language/{os.listdir(f"{memory_dir}/KeyTable_Language")[0]}'


    with open(filepath, 'r') as infile:
        # read the JSON data from the file into a dictionary
        language = json.load(infile)
    return language
