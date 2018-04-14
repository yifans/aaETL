#!/usr/bin/env python
# encoding: utf-8

from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
from etlTask import etl
from config_default import config


minutes = '*/' + str(config['etl']['minutes'])
app = Celery('aaETL')

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'perminute': {
            'task': 'aaETLMain.myTask',
            'schedule': crontab(minute=minutes),
            'args': ''
        }
    }
)

@app.task
def myTask():
    etl()
