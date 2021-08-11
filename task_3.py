from os import  path, walk, listdir
import shutil

project_name = 'new_pj_1'

try:
    for root, dirs, files in walk(project_name):
        if 'temlates' in dirs and root != project_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(project_name, 'templates', entry))
except FileExistsError:
    print("Already works with templates")