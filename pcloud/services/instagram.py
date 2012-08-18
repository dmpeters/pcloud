import pdb



#id 8b6d72cafbfb449fb5330c520b5102ed
#secret 6253323e9e064c10a397698f49c224b3


class Instagram(object):
    
    def __init__(self, token):
        from instagram.client import InstagramAPI
        api = InstagramAPI(access_token=token)
        media = api.user_recent_media()
        pdb.set_trace()