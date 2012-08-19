import os
import json
import urllib2
import gevent
from gevent.pool import Pool
import gevent.monkey
from collections import namedtuple

gevent.monkey.patch_socket()
gevent.monkey.patch_ssl()

DownloadResource = namedtuple('DownloadResource', 'network url')

class DownloadService(dict):

    def __init__(self, notify_service):
        self.notify_service = notify_service

    def start(self, files, receipt):
        meta = {}
        total = 0
        resources = []

        # this will build some meta like:
        # {'facebook':22, 'instagram':10, 'total':32}
        # and it will store the files in a DownloadResource tuple
        # so we can know what kind of resource finished.

        for k, v in files.items():
            resource = DownloadResource(network=k, url=v)
            resources.append(resource)
            count = len(v)
            meta[k] = count
            total = total + count

        meta['total'] = total
        self.notify_service.send_notification('progress_meta', meta)
        pool = Pool(3)
        pool.map(self._fetch_image, resources, receipt)

        # start zipping and transfering to S3 here
        # ... do that ...
        final_data = {'url': 'http://pick-up/your-shit/here.zip'}
        self.notify_service.send_notification('finished', final_data)



    def _fetch_image(self, resource, receipt):
        src = resource.url

        #src = src.replace('https', 'http')

        filename = os.path.basename(src)
        response = urllib2.urlopen(src)

        #where should this be saved?  right now it's just proj_root/out
        # probz should pass the receipt here too so it could be:
        # proj_root/out/{{receipt}}/*
        with open('out/{}/{}'.format(receipt,filename), 'w+') as f:
            f.write(response.read())

        data = {'network': resource.network, 'url': url}
        self.notify_service.send_notification('resource_complete', data)








