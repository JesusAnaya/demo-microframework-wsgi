from framework.response import Response, render_to_response
from framework.request import Request
from framework.utils import import_object
from framework.exceptions import LoginError, NotFoundError
import re


def not_found_404(request):
    return render_to_response('<h1>Page not found.</h1>', status_code=404)


def forbidden_403(request):
    return render_to_response('<h1>403 Forbidden</h1>', status_code=403)


class Router(object):
    settings = None
    routes = {}

    def __init__(self, settings):
        self.settings = settings
        self.routes = getattr(self.settings, 'APP_ROUTES', {})

    def dispatch(self, request):
        try:
            # find view from path in the request
            view_full_path, params = self.find_path_match(request.path)
            view = import_object(view_full_path)

            # request middlewares
            self.request_middlewares(request)

            # excecute view
            response = view(request, **params)

            # response middelwares
            self.response_middlewares(response)
        except Exception as e:
            response = self.handle_exceptions(e, request)

        return response

    def find_path_match(self, path):
        for route in self.routes:
            match = re.match(route[0], path)
            if match:
                return route[1], match.groupdict()

        raise NotFoundError

    def request_middlewares(self, request):
        middlewares_class_paths = getattr(self.settings, 'MIDDLEWARE_CLASSES', [])

        for middleware_class_path in middlewares_class_paths:
            middleware_class = import_object(middleware_class_path)
            middleware_class().before_request(request)

    def response_middlewares(self, response):
        middlewares_class_paths = reversed(
            getattr(self.settings, 'MIDDLEWARE_CLASSES', []))

        for middleware_class_path in middlewares_class_paths:
            middleware_class = import_object(middleware_class_path)
            middleware_class().after_response(response)

    def handle_exceptions(self, exception, request):

        if isinstance(exception, LoginError):
            view = import_object('framework.router.forbidden_403')
            return view(request)

        elif isinstance(exception, NotFoundError):
            view = import_object('framework.router.not_found_404')
            return view(request)
        else:
            raise exception

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch(request)
        return response(environ, start_response)
