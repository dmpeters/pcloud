import pdb
from instagram.client import InstagramAPI
import json
import requests

#id 8b6d72cafbfb449fb5330c520b5102ed
#secret 6253323e9e064c10a397698f49c224b3


class Instagram(object):
    
    def __init__(self, code=None):
        #token = self.get_token(code)
        api = InstagramAPI(client_id='8b6d72cafbfb449fb5330c520b5102ed', client_secret='6253323e9e064c10a397698f49c224b3', redirect_uri='http://127.0.0.1:8000')
        token, user = api.exchange_code_for_access_token(code)
        self.api = InstagramAPI(access_token=token)
        
        
    def get_photos(self):
        photos, next = self.api.user_recent_media()
        
        results = []
        for photo in photos:
             results.append(photo.images['standard_resolution'].url)
        return results
        
        
        