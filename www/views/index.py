import pdb
from instagram.client import InstagramAPI
from .base import BaseView
#from pcloud.services.instagram import Instagram


class IndexView(BaseView):
    def get(self, request):
        ig_token = request.GET.get('ig_token', False) 
        if ig_token:
            api = InstagramAPI(access_token=ig_token)
            media = api.user_recent_media()
            print media
            
        return self.view('index.html', {})