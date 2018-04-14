import datetime
import urllib.parse
import urllib.request

def get_aa_data_txt(host, pv_name, start, end):
    '''
    从aa处获得数据，按照txt格式
    :param host: aa主机名字
    :param pv_name: 查询pv名称
    :param start: 开始时间，datetime格式，utc时间
    :param end: 结束时间，datetime格式，utc时间
    :return: 从aa处获得的数据，list格式
    '''
    url = 'http://' + host + ':17668/retrieval/data/getData.txt'
    start_string = datetime_to_aa_format(start)
    end_string = datetime_to_aa_format(end)
    values = {
        'pv': pv_name,
        'from': start_string,
        'to': end_string
    }
    url_values = urllib.parse.urlencode(values)
    url = url + '?' + url_values
    print(url)
    raw_data = []
    with urllib.request.urlopen(url) as response:
        the_page = response.read()
        data = the_page.decode('utf-8') #转码,否则以‘b开头
        data = data.split('\n') #把一整个字符串转成列表
        raw_data = list(filter(isDataline, data))
        #raw_data = raw_data[2:] # aa返回的数据，每次多多返回一行，所以去掉第一行
    return raw_data

def isDataline(line):
    '''
    删除返回元素行中不是数据的行
    :param line: 从aa处返回的数据行
    :return: 遇到不合条件的列，返回false，否则返回true
    '''
    if line[0:9] == 'Beginning':
        return False
    if line[0:9] == 'Data from':
        return False
    if line == '':
        return False
    return True


def datetime_to_aa_format(thetime):
    time_string = thetime.isoformat()
    time_string = time_string[:-3] + 'Z'
    return time_string


if __name__ == '__main__':
    host = '192.168.113.40'
    pv = 'RNG:BEAM:CURR'
    format = 'txt'
    start_time = datetime.datetime.utcnow() - datetime.timedelta(seconds=60)
    end_time = datetime.datetime.utcnow()
    data = get_aa_data_txt(host, pv, start_time, end_time)
    print(data)
    with open('./test.txt', 'w') as f:
        f.write('\n'.join(data))
