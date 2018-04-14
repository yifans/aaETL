import urllib.parse
import urllib.request
import json


def get_pvlist(host):

    url = 'http://' + host + ':17665/mgmt/bpl/getAllPVs'
    values = {
        'limit': -1
    }
    url_values = urllib.parse.urlencode(values)
    url = url + '?' + url_values
    with urllib.request.urlopen(url) as response:
        the_page = response.read()
        data = the_page.decode('utf-8') #转码,否则以‘b开头
        # data = data.split('\n') #把一整个字符串转成列表
        pvlist = json.loads(data)
        return pvlist


if __name__ == '__main__':
    host = '192.168.113.40'
    pvlist = get_pvlist(host)
    print(pvlist)