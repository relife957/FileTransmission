from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import datetime


def my_job():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BlockingScheduler( executors=executors, job_defaults=job_defaults)
scheduler.add_job(my_job, 'interval', seconds=5,start_date=datetime.datetime.today())

try:
    scheduler.start()
except SystemExit:
    print(111)