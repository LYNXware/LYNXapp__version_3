import os
from pathlib import Path
import json

print("memory.py")

#memory_embedded
#
# base_dir = os.path.dirname(os.path.abspath(__file__))
# print(base_dir)
#
# parent_base_dir = Path(base_dir).parent
# print(parent_base_dir)


app_dir = Path(os.getcwd()).parent
# print(f'get app_dir: {app_dir}')

memory_dir = os.path.join(app_dir, "LYNXapp_Memory")
# print(memory_dir)

if not os.path.exists(memory_dir):
    print("memory.py -> create 'memory' directory ")
    os.makedirs(memory_dir)

    # and pass the files from embedded memory

else:
    print("memory.py -> directory  'memory'  exists")





# Function to save data to a file
def save_data(data, file):

    filepath = os.path.join(memory_dir, file)
    print(f'memory.py -> save_data: {file}  {data}')

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


# Function to load data from a file
def load_data(file):

    filepath = os.path.join(memory_dir, file)
    print(f'memory.py -> load_data: {filepath}')

    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None



# #test
# data_test = {"key": "value02"}
# test_file = "tf000.json"
#
# save_data(data_test, test_file)
# loaded_data_test = load_data(test_file)
#
# print(f'memory.py -> loaded_data_test: {loaded_data_test}')

