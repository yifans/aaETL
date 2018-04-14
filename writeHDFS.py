import pyhdfs
from config_default import config


def write_hdfs(path, content):
    host = config['hdfs']['host']
    port = config['hdfs']['port']
    hosts = host + ':' + port
    user = config['hdfs']['user']

    fs = pyhdfs.HdfsClient(hosts=hosts, user_name=user)
    if not fs.exists(path):
        fs.create(path, '')
    fs.append(path, content)

if __name__ == '__main__':
    write_hdfs('/hals/aaRawData/RNG:BEAM:CURR.txt', 'hello world')
