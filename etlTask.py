import datetime

from getPVList import get_pvlist
from writeHDFS import write_hdfs
from writeLocal import write_local
from getDataFromAA import get_aa_data_txt
from config_default import config


def etl():
    minutes = config['etl']['minutes']
    start_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes)
    start_timestamp = int(start_time.timestamp())
    end_time = datetime.datetime.utcnow()
    end_timestamp = int(end_time.timestamp())
    if not end_time.second == 0:  # 如果不是整分钟数，就不执行etl
        return
    # pvlist = ['RNG:IVU:BPM:BPM2:X']
    pvlist = get_pvlist(config['aa']['host'])
    for pvitem in pvlist:
        content = get_aa_data_txt(config['aa']['host'], pvitem, start_time, end_time)
        pv_name = pvitem.replace(':', '@') # hdfs上文件不能含有：，将pv中：替换为@
        file_name = pv_name \
                    + '%' + str(start_timestamp) \
                    + '%' + str(end_timestamp) \
                    + '.txt'
        if config['mode'] == 'local':
            local_path = config['local']['path'] + '/' + pv_name + '/' + file_name
            write_local(local_path, content)
        if config['mode'] == 'hdfs':
            hdfs_path = config['hdfs']['path'] + '/' + pv_name + '/' + file_name
            write_hdfs(hdfs_path, content)


if __name__ == '__main__':
    etl()
