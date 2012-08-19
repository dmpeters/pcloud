import logging
import gevent
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

    def on_register(self, receipt):
        print('Receipt', receipt)
        #self.emit('welcome', message)

        return True
