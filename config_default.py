config = {
    'mode': 'local', # 'local' or 'hdfs'
    'etl': {
        'minutes': 1
    },
    'hdfs': {
        'host': '192.168.113.41',
        'port': '50070',
        'user': 'pengquan.wen',
        'path': '/hals/aaRawData'
    },
    'aa': {
        'host': '192.168.113.40'
    },
    'local': {
       'path': '/tmp/aa'
    }
}
