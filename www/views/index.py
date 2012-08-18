from .base import BaseView


class IndexView(BaseView):
    def get(self, request):
        return self.view('index.html', {})