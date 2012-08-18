import requests, json, pdb

class Facebook(object):
	
	def __init__(self, code=None):
		app_id = '230178707104819'
		app_secret = '7fc59c3c5a7800804b73e9d2c1006d05'
		app_redirect_url = 'http://127.0.0.1:8000'
		app_scope = 'id, user_photos'
		token = token
		self.get_photos()
	
	def get_photos(self, id, albums):
		
		# Get Photos
		query = 'https://graph.facebook.com/fql?q=\
				SELECT src_big FROM photo WHERE aid IN (\
				SELECT aid FROM album WHERE owner=me()\
				&access_token={})'.format(token)
		q = requests.get(query)
		photos = q