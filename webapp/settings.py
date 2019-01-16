

MIDDLEWARE_CLASSES = [
    'webapp.middlewares.SessionMiddleware'
]


APP_ROUTES = {
    '/': 'webapp.views.home_view'
}
