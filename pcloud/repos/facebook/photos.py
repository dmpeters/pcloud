import requests, json, pdb

class Facebook(object):
	
	def __init__(self, token=None):
		self.app_id = '230178707104819'
		self.app_secret = '7fc59c3c5a7800804b73e9d2c1006d05'
		self.app_redirect_url = 'http://127.0.0.1:8000'
		self.app_scope = 'id, user_photos'
		self.token = token
	
	def get_photos(self):
		
		# Get Photos
		fql_url = 'http://graph.facebook.com/fql?q=\
					SELECT+src_big+FROM+photo+WHERE+aid+IN+(\
					SELECT+aid+FROM+album+WHERE+owner=me())\
					&access_token={}'.format(self.token)
		q = requests.get(fql_url)
		photos = q.json
		response = []
		for img in photos['data']:
			response.append(img['src_big'])
		return response