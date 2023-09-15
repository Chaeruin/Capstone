from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_temperature, get_humidity

def update_num():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_temperature, 'interval', seconds=60)
    scheduler.add_job(get_humidity, 'interval', seconds=60)
    scheduler.start()