import pyhdfs
import os
from config_default import config


def write_hdfs(path, content):
    host = config['hdfs']['host']
    port = config['hdfs']['port']
    hosts = host + ':' + port
    user = config['hdfs']['user']

    fs = pyhdfs.HdfsClient(hosts=hosts, user_name=user)

    (basename, filename) = os.path.split(path)
    if not fs.exists(basename):
        fs.mkdirs(basename)
    if not fs.exists(path):
        fs.create(path, '')
    fs.append(path, content)

if __name__ == '__main__':
    write_hdfs('/hals/aaRawData/RNG@IVU@BPM@BPM2@X/RNG@IVU@BPM@BPM2@X%1523906040%1523906100.txt', 'hello world')
    # write_hdfs('/hals/aaRawData/RNG:BEAM:CURR.txt', 'hello world')
