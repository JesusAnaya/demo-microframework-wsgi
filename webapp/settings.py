

MIDDLEWARE_CLASSES = [
    'webapp.middlewares.SessionMiddleware'
]


APP_ROUTES = (
    (r'^/$', 'webapp.views.home_view'),
    (r'^/page/(?P<id>\d+)/$', 'webapp.views.page'),
)
