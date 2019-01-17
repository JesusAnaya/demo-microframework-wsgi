from framework.response import render_to_response


def home_view(request):
    return render_to_response('<h1>Hello World!</h1>', status_code=200)


def page(request, id):
    return render_to_response('<h1>Page id = {0}</h1>'.format(id), status_code=200)
