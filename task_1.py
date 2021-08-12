import os
import shutil
list_dir = ['settings', 'mainapp', 'adminapp', 'authapp', 'lol']

shutil.rmtree('my_project')

os.makedirs('my_project')
os.chdir('my_project')

for folder in sorted(list_dir, reverse=True):
    os.mkdir(folder)