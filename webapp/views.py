from framework.response import render_to_response
from framework.utils import load_template

def home_view(request):
    template = load_template("home.html")
    return render_to_response(template, status_code=200)


def hello(request, name):
    template = load_template("hello.html", {'name': name})
    return render_to_response(template, status_code=200)


def not_found_404(request):
    template = load_template("error404.html")
    return render_to_response(template, status_code=404)


def forbidden_403(request):
    template = load_template("error403.html")
    return render_to_response(template, status_code=403)
