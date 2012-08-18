import pdb
from .base import BaseView
from pcloud.ioc import container


class IndexView(BaseView):
    def get(self, request):
        ig_token = request.GET.get('ig_token', False) 
        if ig_token:
            i = container.Instagram(access_token=ig_token)
            
            
        return self.view('index.html', {})