import datetime

from getPVList import get_pvlist
from writeHDFS import write_hdfs
from writeLocal import write_local
from getDataFromAA import get_aa_data_txt
from config_default import config


def etl():
    minutes = config['etl']['minutes']
    start_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes)
    end_time = datetime.datetime.utcnow()
    if not end_time.second == 0: #如果不是整分钟数，就不执行etl
        print('pass')
        return
    # print('elt')
    # pvlist = ['RNG:BEAM:CURR','RNG:BEAM:LIFE']
    # pvlist = ['RNG:BEAM:CURR']
    # pvlist = ['RNG:WIG:BPM:BPM2:X']
    pvlist = ['RNG:IVU:BPM:BPM2:X']
    # pvlist = get_pvlist(config['aa']['host'])
    for pvitem in pvlist:
        content_list = get_aa_data_txt(config['aa']['host'], pvitem, start_time, end_time)
        content = '\n'.join(content_list)
        content += '\n'
        content += '---> content\n'
        local_path = config['local']['path'] + '/' + pvitem + '.txt'
        hdfs_path = config['hdfs']['path']  + '/' + pvitem + '.txt'
        write_local(local_path, content)
        #write_hdfs(hdfs_path,content)
        # print('--> write' + path)

if __name__ == '__main__':
    etl()
