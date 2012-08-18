import requests
import pdb

class DjangoFacebookPhotos(object):
	
	def __init__(self):
		self._app_id = '230178707104819'
		self._app_secret = '7fc59c3c5a7800804b73e9d2c1006d05'
		self._app_redirect_url = 'http://127.0.0.1:8000'
		self._app_scope = 'id, user_photos'
	
	def access_token(self):
		url = 'https://www.facebook.com/dialog/oauth?\
				client_id={}&\
				redirect_uri={}&\
				scope={}&\
				state={}'.format(self._app_id, self._app_redirect_url, self._app_scope)
		r = requests.get(url)
	
	def get_albums(self, id, token):
		# todo GET/REQUEST TOKEN
		table =  'album'
		query = 'https://graph.facebook.com/fql?\
				q=SELECT+aid+FROM+{}+WHERE+\
				uid1=me()&{}'.format(album, token)
		q = requests.get(query)
		albums = q
		
		album_books = []
		for album in albums['data']:
			book = {}
			book['aid'] = album['aid']
			album_books.append(book)
		return album_books
	
	def get_photos(self, id, albums):
	
	