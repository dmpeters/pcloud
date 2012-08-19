from __future__ import absolute_import
import json
import redis


class RedisNotifications(object):

    def __init__(self, channel):
        self.redis_conn = redis.Redis()
        self.channel = channel
        #pubsub = self.redis_conn.pubsub()
        #pubsub.subscribe(channel)

    def send_notification(self, event, data=None):
        message = "%s|%s" % (event, json.dumps(data))
        print("sending notification to channel: ", self.channel)
        self.redis_conn.publish(self.channel, message)