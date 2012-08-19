import os
import json
import urllib2
import gevent
from gevent.pool import Pool
import gevent.monkey

class DownloadService(obj):
    
    def __init__(self, download_arr, receipt):
        self.download_arr = download_arr
        self.receipt = receipt
        gevent.monkey.patch_socket()
    
    def start(self):
        pass
    
    def _fetch_image(url):
        src = url.replace('https', 'http')
        
        filename = os.path.basename(src)
        response = urllib2.urlopen(src)

        with open('out/%s' % filename, 'w+') as f:
            f.write(response.read())
        
        
        
#if __name__ == "__main__":
#    pool = Pool(3)
#    data = None
#
#    with open('images.json') as f:
#        data = json.loads(f.read())
#
#    pool.map(fetch_image, data['data'])
#    print ('ALL DONE')





