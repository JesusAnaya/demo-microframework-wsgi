from framework.config import Configurator
from webapp import settings

config = Configurator(settings)
app = config.make_wsgi_app()
