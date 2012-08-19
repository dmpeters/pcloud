class NotificationService(object):

    def __init__(self, dao):
        self.dao = dao
        self.channel = None

    def send_notification(self, event, data=None):
        self.dao.send_notification(event, data)