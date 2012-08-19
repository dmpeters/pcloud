import os
import tarfile
import boto
from boto.s3.key import Key
from www import settings


class ZipS3(object):
    
    
    def zip(self, images, receipt):
        zip_name = "{}.tar.gz".format(receipt)
        zip_path = 'out/'+ zip_name
        tar = tarfile.open(zip_path, "w:gz")
        for image in images:
            tar.add(image)
        tar.close()
        for image in images:
            os.remove(image)
        
        conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        k = Key(bucket)
        k.key = zip_name
        k.set_contents_from_filename(zip_path)
        k.set_acl('public-read')
        response = 'https://s3.amazonaws.com/' +settings.AWS_STORAGE_BUCKET_NAME +'/' +zip_name
        
        os.remove(zip_path)
        
        return response
        
        