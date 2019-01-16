from framework.response import render_to_response

def home_view(request):
    return render_to_response('<h1>Hello World!</h1>', status_code=200)
