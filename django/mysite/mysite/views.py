from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context

def hello(req):
    #import pdb; pdb.set_trace()
    return HttpResponse("Hello World!")

def time(req):
    now = datetime.datetime.now()
    html = "Server time:%s" %now
    return HttpResponse(html)

def hours_ahead(req,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "Now is: %s .<br>In %s hour(s), it will be: %s ." %(datetime.datetime.now(),offset,dt)
    return HttpResponse(html)
