import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

MIDDLEWARE_CLASSES = [
    'webapp.middlewares.SessionMiddleware'
]

APP_ROUTES = (
    (r'^/$', 'webapp.views.home_view'),
    (r'^/hello/(?P<name>[\w\s\+]+)/$', 'webapp.views.hello'),
)

PATH_VIEW_NOT_FOUND_404 = 'webapp.view.not_found_404'
PATH_VIEW_FORBIDDEN_403 = 'webapp.view.forbidden_403'
