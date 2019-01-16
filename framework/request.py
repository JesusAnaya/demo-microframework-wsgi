
class Request(object):
    method = 'GET'
    path = '/'
    query_string = ''
    cookies = {}

    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        self.query_string = environ['QUERY_STRING']

        for raw_cookie in environ.get('HTTP_COOKIE', '').split('; '):
            key, value = raw_cookie.split('=', 1)
            cookie = {key: value}
            self.cookies.update(cookie)
