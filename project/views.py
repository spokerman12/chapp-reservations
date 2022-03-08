from django.http import HttpResponse

def index(request, data = None):
    return HttpResponse("Hello World %s." % data)

