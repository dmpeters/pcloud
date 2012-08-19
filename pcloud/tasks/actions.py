from celery import task
from pcloud.ioc import container
from pcloud.services.notifications import NotificationService
from pcloud.repos.notifications.redis import RedisNotifications
from pcloud.services.download import DownloadService

@task
def get_photos(receipt, instagram=None, facebook=None):
    
    notify = NotificationService(RedisNotifications(receipt))
    #TODO send soemthing to adam saying started
    notify.send_notification('event_string', {})
    
    photos = []
    if facebook:
        fb = container.Facebook(token=facebook)
        photos += fb.get_photos()
    
    if instagram:
        ig = container.Instagram(code=instagram)
        photos += ig.get_photos()
        
        
    dl = DownloadService(photos,notify)
    dl.start()
    
    
    
    
    
    # twitter.s(show_schedule.show).apply_async()
    # facebook.s(show_schedule.show).apply_async()
    # get_glue.s(show_schedule.show).apply_async()

    # now = make_naive(datetime.utcnow().replace(tzinfo=utc), pytz.utc)
    # stop_time = make_naive(show_schedule.start_date + timedelta(minutes=show_schedule.run_for),pytz.utc)
    # if now < stop_time:
    #     again = now + timedelta(seconds=60)
    #     start_show_polling.apply_async([show_schedule],eta=again)