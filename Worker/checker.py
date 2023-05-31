from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from Worker import work


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(work.handler, 'interval', minutes=1, max_instances=1, replace_existing=True)
   
    
    scheduler.start()
    scheduler.shutdown()
    scheduler.remove_all_jobs()