import pdb
from .base import BaseView
from pcloud.ioc import container


class IndexView(BaseView):
	def get(self, request):
		
		ig_code = request.GET.get('ig_code', False)
		fb_code = request.GET.get('fb_code', False)
		
		if ig_code:
			i = container.Instagram(code=ig_code)
		
		if fb_code:
			f = container.Facebook(token=fb_code)
		
		return self.view('index.html', {})