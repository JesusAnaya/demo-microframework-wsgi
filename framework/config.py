from framework.router import Router

settings = {}


class Configurator(object):
    settings = None

    def __init__(self, settings):
        self.settings = settings

    def make_wsgi_app(self):
        global settings
        app = Router(self.settings)
        settings = self.settings
        return app
