import logging
import json
import gevent
import redis
from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace


@namespace('/status')
class StatusNamespace(BaseNamespace):

    def initialize(self):
        pass
        #self.logger = logging.getLogger("socketio.status")
        #self.log("Socketio session started")

    def log(self, message):
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))

    def on_register(self, token):

        self.redis_conn = redis.Redis()
        pubsub = self.redis_conn.pubsub()

        gevent.spawn(self.sub, pubsub, token)

        return True

    def recv_disconnect(self):
        self.disconnect(silent=True)
        return True

    def sub(self, pubsub, token):

        pubsub.subscribe(token)

        for msg in pubsub.listen():
            data = None

            try:
                data = json.loads(msg['data'])
            except TypeError:
                pass

            if data:
                try:
                    event = data['event']
                    data = data['data']
                    gevent.spawn(self.emit, event, json.dumps(data))
                    #self.emit(event, json.dumps(data))
                except KeyError:
                    pass

            gevent.sleep(0)
