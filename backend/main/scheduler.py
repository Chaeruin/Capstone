# scheduler.py

from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler import util

def my_job():
    # APScheduler 작업으로 실행할 로직을 작성합니다.
    pass

util.register_job(
    my_job,
    'interval',
    seconds=10,  # 10초마다 실행
    id='my_job',  # 작업 ID
    replace_existing=True,
    jobstore=DjangoJobStore(),
)
