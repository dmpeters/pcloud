from pydi import Container
from pcloud.repos.instagram.photos import Instagram
from pcloud.repos.facebook.photos import Facebook

container = Container()
container.register(Instagram)
container.register(Facebook)

