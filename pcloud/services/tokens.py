import os

class TokenService(object):

    def token(self):
        return os.urandom(16).encode('hex')