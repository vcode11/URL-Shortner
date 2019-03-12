from django.shortcuts import render, redirect
from .models import URL
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SubmitURLForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .code_generator import generate


@login_required(login_url='/login/')
def index(request):
    if request.method == "GET":
        form = SubmitURLForm(request.GET)
        context = {
            'form': form,
            'title': 'URL Shortner'
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
                    'form': form,
                    'title': 'URL Shortner',
                    'shortened_url': 'http://127.0.0.1:8000/'+code,
                }
                return render(request, 'shortner/index.html', context)
            while True:
                code = generate(6)
                try:
                    urlobj = URL.objects.get(short_url=code)
                except:
                    break
            url = URL(
                full_url=form.cleaned_data['URL_Field'], short_url=code, user=request.user)
            url.save()
        context = {
            'form': form,
            'title': 'URL Shortner',
            'shortened_url': 'http://127.0.0.1:8000/' + code,
        }
    return render(request, 'shortner/index.html', context)


def redirect(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
    except:
        return HttpResponse("Page you were looking for was not found on our sever")
    url.clicks += 1
    url.save()
    return (HttpResponseRedirect(url.full_url))


def userlogin(request):
    if request.method == 'GET':
        context = {
            'could_not_log_in': False,
        }
        return render(request, 'shortner/login.html', context)
    else:
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            context = {
                'could_not_log_in': True,
            }
        return render(request, 'shortner/login.html', context)


def userlogout(request):
    logout(request)
    context = {
        'could_not_log_in': False
    }
    logout(request)
    return HttpResponseRedirect('/login')


def usersignup(request):
    if request.method == 'GET':
        form = SignupForm(request.GET)
        return render(request, 'shortner/signup.html', {'form': form})
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            # if username is taken
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
            except:
                pass
            else:
                error_message = 'Username %s is already taken.' % (
                    form.cleaned_data['username'])
                return render(request, 'shortner/signup.html', {'form': form, 'error_message': error_message})

            try:
                user = User.objects.get(email=form.cleaned_data['email'])
            except:
                pass
            else:
                error_message = 'Email %s is already being used.' % (
                    form.cleaned_data['email'])
                return render(request, 'shortner/signup.html', {'form': form, 'error_message': error_message})
            # if passwords match
            if form.cleaned_data['password'] == form.cleaned_data['confirmPassword']:
                user = User.objects.create_user(
                    form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                user.save()
                return render(request, 'shortner/signup.html', {'form': form, 'error_message': 'Account created successfully'})
            else:
                error_message = 'Passwords don\'t match.'
                return render(request, 'shortner/signup.html', {'form': form, 'error_message': error_message})
