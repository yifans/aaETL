import os


def write_local(path, content):
    (basename, filename) = os.path.split(path)
    if not os.path.exists(basename):
        os.makedirs(basename)
    with open(path, 'a') as f:
        f.write(content)