from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm
from django.views.decorators.http import require_POST,require_http_methods, require_safe
from django.contrib.auth.decorators import login_required 

# Create your views here.
@require_safe
def index(request):
    return render(request, 'articles/index.html')

@require_http_methods(['POST','GET'])
def signup(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['POST','GET'])
def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
@require_POST
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('articles:index')

@login_required
@require_http_methods(['POST','GET'])
def update(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method =="POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context={
        'form':form,
    }    
    return render(request, 'accounts/update.html', context)

@login_required
@require_http_methods(['POST','GET'])
def password(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method =="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context={
        'form':form,
    }
    return render(request, 'accounts/password.html', context)


def delete(request):
    request.user.delete()
    return redirect('articles:index')