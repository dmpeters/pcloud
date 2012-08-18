import requests, json, pdb

class Facebook(object):
	
	def __init__(self, code=None):
		app_id = '230178707104819'
		app_secret = '7fc59c3c5a7800804b73e9d2c1006d05'
		app_redirect_url = 'http://127.0.0.1:8000'
		app_scope = 'id, user_photos'
		token = ''
	
	def get_photos(self, id, albums):
		
		# Get Photo Albums
		table =  'album'
		#TODO: Fix Query - this will fail
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
		
		# Get Photos
		fb_photos = []
		for album in album_books:
			#TODO: correct fql query for photos
			photos = 'query album for photos'
			p = requests.get(query)
				