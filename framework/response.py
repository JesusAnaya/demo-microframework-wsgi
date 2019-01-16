from pprint import pprint

class Response(object):
    status = '200 OK'
    headerlist = [('Content-Type', 'text/html; charset=UTF-8')]
    body = b''

    def __call__(self, environ, start_response):
        self.headerlist.append(('Content-Length', str(len(self.body))))
        start_response(self.status, self.headerlist)
        return [self.body]


def render_to_response(body_html, status_code=200):
    response = Response()

    if status_code == 200:
        response.status = '200 OK'

    if status_code == 400:
        response.status = '400 Bad Request'

    if status_code == 404:
        response.status = '404 Not Found'

    if status_code == 403:
        response.status = '403 Forbidden'

    response.body = body_html.encode()

    return response
