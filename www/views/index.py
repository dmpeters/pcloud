from .base import BaseView
from pcloud.services.instagram import Instagram


class IndexView(BaseView):
    def get(self, request):
        i = Instagram(token='tokenhere')
        return self.view('index.html', {})