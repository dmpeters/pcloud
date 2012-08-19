from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
import boto

class Facebook(object):
	
	def __init__(self):
		self.as3_access = ''
		self.as3_secret = ''
		self.zip()
	
	def zip(self, images, receipt):
		
		# generate zip
		zipped = HttpResponse(FileWrapper(images), content_type='application/zip')
		zipped['Content-Disposition'] = 'attachment; filename={}.zip'.format(receipt)
		
		# s3 storage
		conn = boto.connect_s3('{}','{}').format(self.as3_access, self.as3_secret)
		bucket = conn.create_bucket('{}_pcloud').format(self.as3_access)
		pkey = Key(bucket)
		pkey = receipt
		pkey.set_contents_from_file(zipped, replace=True, cb=None, num_cb=10)
		
		
		''' 
			generate_url(21600, method='GET') - ?
			complete_upload()
		'''