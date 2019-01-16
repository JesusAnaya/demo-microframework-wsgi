from framework.response import Response, render_to_response
from framework.request import Request
from framework.utils import import_object


def view_404(request):
    return render_to_response('<h1>Page not found.</h1>', status_code=404)


class Router(object):
    settings = None
    routes = {}

    def __init__(self, settings):
        self.settings = settings
        self.routes = getattr(self.settings, 'APP_ROUTES', {})

    def dispatch(self, request):

        try:
            # request middlewares
            self.request_middlewares(request)

            view_full_path = self.routes.get(request.path, 'framework.router.view_404')
            view = import_object(view_full_path)
            response = view(request)

            # response middelwares
            self.response_middlewares(response)
        except Exception as e:
            response = self.handle_exceptions(e)

        return response

    def request_middlewares(self, request):
        middlewares_class_paths = getattr(self.settings, 'MIDDLEWARE_CLASSES', [])

        for middleware_class_path in middlewares_class_paths:
            middleware_class = import_object(middleware_class_path)
            middleware_class().before_request(request)

    def response_middlewares(self, response):
        middlewares_class_paths = reversed(getattr(self.settings, 'MIDDLEWARE_CLASSES', []))

        for middleware_class_path in middlewares_class_paths:
            middleware_class = import_object(middleware_class_path)
            middleware_class().after_response(response)

    def handle_exceptions(self, exception):
        from framework.exceptions import LoginError

        if isinstance(exception, LoginError):
            return render_to_response('<h1>Forbidden</h1>', status_code=403)
        else:
            raise exception

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch(request)
        return response(environ, start_response)
