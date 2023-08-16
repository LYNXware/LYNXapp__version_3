import os
from pathlib import Path
import json

print("memory.py")




#memory_embedded




memory_dir = os.path.join(os.pardir, "LYNXapp_Memory")
print(memory_dir)

if not os.path.exists(memory_dir):
    print("create 'memory' directory ")
    os.makedirs(memory_dir)

    # and pass the files from embedded memory

else:
    print("directory  'memory'  exists")



# base_dir = os.path.dirname(os.path.abspath(__file__))
# parent_base_dir = Path(base_dir).parent
# print(base_dir)
# print(parent_base_dir)
# x = os.pardir
# print(x)
# z = os.path.join(os.getcwd(), os.pardir)
# print(z)
# z1 = os.path.join(z, 'file.txt')
# print(z1)
# app_dir = Path(os.getcwd()).parent
# print(app_dir)
# memory_dir = os.path.join(app_dir, "memory")
# print(memory_dir)
# if not os.path.exists(memory_dir):
#     print("Creating directory")
#     os.makedirs(memory_dir)
# else:
#     print("Directory exists")#
# test = os.pardir
# test_dir = os.path.join(test, "test")
# print(test_dir)
# if not os.path.exists(test_dir):
#     print("test Creating directory ")
#     os.makedirs(test_dir)
# else:
#     print("test Directory exists")