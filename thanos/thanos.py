import os
import random
from shutil import rmtree

def snap(directory):
    files = os.listdir(directory)
    to_delete = random.sample(files, len(files) // 2)

    for file in to_delete:
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            rmtree(path)

if __name__ == "__main__":
    snap(os.getcwd())
