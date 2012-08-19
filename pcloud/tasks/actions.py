from celery import task
from pcloud.ioc import container
from pcloud.services.notifications import NotificationService
from pcloud.repos.notifications.redis import RedisNotifications
from pcloud.services.download import DownloadService

@task
def get_photos(receipt, instagram=None, facebook=None):
    notify = NotificationService(RedisNotifications(receipt))
    #TODO send soemthing to adam saying started
    # notify.send_notification('event_string', {})

    photos = {'facebook':[], 'instagram': []}

    fb_photos = photos['facebook']
    ig_photos = photos['instagram']

    if facebook:
        fb = container.Facebook(token=facebook)
        fb_photos += fb.get_photos()

    if instagram:
        ig = container.Instagram(code=instagram)
        #ig_photos += ig.get_photos()
    
    dl = DownloadService(notify)
    dl.start(photos, receipt)
    print 'done!'
    
