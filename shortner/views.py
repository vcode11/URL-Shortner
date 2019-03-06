from django.shortcuts import render
from .models import URL
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SubmitURLForm

from .code_generator import generate

def index(request):
    if request.method == "GET":
        form = SubmitURLForm(request.GET)
        context = {
            'form':form,
            'title':'URL Shortner'
        } 
    else:
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            try:
                url = URL.objects.get(full_url=form.cleaned_data['URL_Field'])
            except:
                pass
            else:
                code = url.short_url
                context = {
                    'form':form,
                    'title':'URL Shortner',
                    'shortened_url':'http://127.0.0.1:8000/'+code,
                    }
                return render(request, 'shortner/index.html', context) 
            while True:
                code = generate(6)
                try:
                    urlobj = URL.objects.get(short_url=code)
                except:
                    break
            url = URL(full_url=form.cleaned_data['URL_Field'],short_url=code)
            url.save()
        context = {
            'form':form,
            'title':'URL Shortner',
            'shortened_url':'http://127.0.0.1:8000/' + code,
        }    
    return render(request, 'shortner/index.html', context)

def redirect(request,short_url):
    try:
        url = URL.objects.get(short_url=short_url)
    except:
        return HttpResponse("Page you were looking for was not found on our sever")
    url.clicks+=1
    url.save()
    return (HttpResponseRedirect(url.full_url))    
