import os.path
import os


names_dir = ['settings','mainapp','adminapp','authapp']


for dir in names_dir:
    path = os.path.join('.','my_project',dir)
    path = os.path.abspath(path)
    os.makedirs(path,exist_ok=True)

