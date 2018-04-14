def write_local(path, content):
    with open(path, 'a') as f:
        f.write(content)