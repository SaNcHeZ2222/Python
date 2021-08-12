import os
import shutil

os.chdir('my_project')

for folder in os.listdir():
    shutil.copytree(folder, f'/Users/admin/PycharmProjects/pythonlearn/my_project/templates/{folder}')
    os.chdir('/Users/admin/PycharmProjects/pythonlearn/my_project')