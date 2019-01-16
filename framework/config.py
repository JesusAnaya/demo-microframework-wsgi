from framework.router import Router

class Configurator(object):
    settings = None

    def __init__(self, settings):
        self.settings = settings

    def make_wsgi_app(self):
        app = Router(self.settings)
        return app
