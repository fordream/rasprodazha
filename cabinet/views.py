from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    post_login = request.POST.get('username', '')
    post_email = request.POST.get('email', '')
    post_password1 = request.POST.get('password', '')
    post_password2 = request.POST.get('password-duplicate', '')
    if post_password1 != post_password2 or post_login == '' or post_email == '':
        return render(request, 'cabinet/register.html', {})
    if len(post_login) > 5 and len(post_email) > 5 and len(post_password1) > 5:
        print(post_login, post_email, post_password1)
        user = User.objects.create_user(post_login, post_email, post_password1)
        user.save()
        return redirect('/cabinet/')
    return render(request, 'cabinet/register.html', {})
