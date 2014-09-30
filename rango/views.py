from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.forms import CategoryForm

from rango.models import Category, Page


def index(request):
    #obtains the context from the http request
    context = RequestContext(request)
    
    #db query, all categories stored, order by likes desc, top 5
    #put in the context dict, which is really like instance to view
    category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list}

    for category in category_list:
        category.url = category.name.replace(' ', '_')

    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "SERIOUSLY ON THE REG."}
    return render_to_response('rango/about.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)

    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}
    
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)

def add_category(request):
    context = RequestContext(request)

    if request.method == 'POST':

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
            form = CategoryForm()

    return render_to_response('rango/add_category.html', {'form': form}, context) 
