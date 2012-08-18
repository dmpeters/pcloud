import requests

class DjangoFacebookPhotos(object):
	
	def __init__(self):
		self._app_id = '230178707104819'
		self._app_secret = '7fc59c3c5a7800804b73e9d2c1006d05'
		self._app_redirect_url = 'http://127.0.0.1:8000'
		self._app_scope = 'user_photos'
		self._app_state = 'u942146p6o91u9'
	
	def access_token(self):
		url =	'https://www.facebook.com/dialog/oauth?\
				client_id={}&\
				redirect_uri={}&\
				scope={}&\
				state={}'.format(self._app_id, self._app_redirect_url, self._app_scope, self._app_state)
		
		r = requests.get(url)
		return r.text.split('=')[1];
	
	def getAlbums(self):
	
	def getPhotos(self):
	
	