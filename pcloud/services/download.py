import os
import urllib2
import gevent
from gevent.pool import Pool
import gevent.monkey
from collections import namedtuple
from pcloud.repos.zip.s3zip import ZipS3

gevent.monkey.patch_socket()
gevent.monkey.patch_ssl()

DownloadResource = namedtuple('DownloadResource', 'network url receipt')


class DownloadService(dict):

    def __init__(self, notify_service):
        self.notify_service = notify_service
        self.local_path_arr = []

    def start(self, files, receipt):
        meta = {}
        total = 0
        resources = []

        # this will build some meta like:
        # {'facebook':22, 'instagram':10, 'total':32}
        # and it will store the files in a DownloadResource tuple
        # so we can know what kind of resource finished.

        for k, v in files.items():
            for url in v:
                resource = DownloadResource(network=k, url=url, receipt=receipt)
                resources.append(resource)
            count = len(v)
            meta[k] = count
            total = total + count

        meta['total'] = total
        
        self.notify_service.send_notification('progress_meta', meta)
        pool = Pool(3)
        pool.map(self._fetch_image, resources)

        # start zipping and transfering to S3 here
        z = ZipS3()
        zip_path = z.zip(self.local_path_arr,receipt)
        final_data = {'url': zip_path}
        self.notify_service.send_notification('finished', final_data)

    def _fetch_image(self, resource):
        src = resource.url
        #receipt = resource.receipt

        filename = os.path.basename(src)
        response = urllib2.urlopen(src)

       #where should this be saved?  right now it's just proj_root/out
       # probz should pass the receipt here too so it could be:
       # proj_root/out/{{receipt}}/*
        os.mkdir('out')
        local_path = 'out/{}'.format(filename) 
        self.local_path_arr.append(local_path)
        with open(local_path, 'w+') as f:
            f.write(response.read())
        
        data = {'network': resource.network, 'url': resource.url}
        gevent.spawn(self.notify_service.send_notification, 'resource_complete', data)
        #self.notify_service.send_notification('resource_complete', data)
