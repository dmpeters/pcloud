import pdb
from .base import BaseView
from pcloud.ioc import container


class IndexView(BaseView):
	def get(self, request):
		return self.view('index.html')
	
	def post(self,request):
		ig_code = request.POST.get('ig_code', False)
		fb_code = request.POST.get('fb_code', False)
		
		if ig_code:
			i = container.Instagram(code=ig_code)
		
		if fb_code:
			f = container.Facebook(token=fb_code)
			
		viewmodel = {'downloading':True}
		#THIS GETS CALLED BY AJAX...adam?  how u wanna deal w/ this?
		return self.view('index.html')