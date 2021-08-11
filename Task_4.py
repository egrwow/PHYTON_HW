import os
import django
from collections import defaultdict

def dir_info():
    root_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dict, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            django_files[size] += 1

    for size, num in sorted(django_files.items()):
        print(f'{size}: {nums}')
