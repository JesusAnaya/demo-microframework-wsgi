from framework.config import Configurator
from webapp import settings


def main():
    config = Configurator(settings)
    return config.make_wsgi_app()

if __name__ == '__main__':
    main()
