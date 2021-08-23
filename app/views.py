from app.models import Blog, Image, Rdv
from app.forms import senderSms, blogForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, authenticate, logout
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    
    send_mail(subject='A cool subject',message='A stunning message',from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])

    context = {
    }

    return render(request, 'home.html', context)


def sender(request):


    return redirect('/')


def hijama(request):

    context = {
        
    }

    return render(request, 'hijama.html', context)


def galerie(request):

    photo = Image.objects.all()

    context = {
        'pics': photo
    }

    return render(request, 'galerie.html', context)

def contact(request):

    context = {
        
    }

    return render(request, 'contact.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('/dashboard')
        else:
            return redirect('/login')

    return render(request, 'admin/signin.html', {})

@login_required
def dashboard(request):

    context = {

    }

    return render(request, 'admin/portail.html', context)

@login_required
def blog(request):

    article = Blog.objects.all()

    context = {
        'blog': article
    }

    return render(request, 'admin/blog.html', context)

@login_required
def blogFormer(request):
    if request.method == 'POST':
        form = blogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    else:
        form = blogForm()
        
    context = {
        'form': form
    }

    return render(request, 'admin/addblog.html', context)

def logoutPage(request):
    
    logout(request)
    return redirect('/login')