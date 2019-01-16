from framework.exceptions import LoginError

FIXED_SESSION = '2c03799f-01e6-4417-8153-887cf6792e81'


class SessionMiddleware(object):
    def before_request(self, request):
        session = request.cookies.get('session')
        if session and session != FIXED_SESSION:
            raise LoginError

    def after_response(self, response):
        pass
