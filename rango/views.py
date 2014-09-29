from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.models import Category


def index(request):
    #obtains the context from the http request
    context = RequestContext(request)
    
    #db query, all categories stored, order by likes desc, top 5
    #put in the context dict, which is really like instance to view
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "SERIOUSLY ON THE REG."}
    return render_to_response('rango/about.html', context_dict, context)

