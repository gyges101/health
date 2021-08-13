from app.models import Blog, Image, Rdv
from app.forms import senderSms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, authenticate, logout
import telnyx

telnyx.api_key = "KEY017B187CE2B994C15ADF807ADF06BFD9_R4zGkrl9p3r9HiADH4IFDh"

your_telnyx_number = "+13125300760"
destination_number = "+212777338028"


# Create your views here.

def home(request):

    if request.method == 'POST':

        send = senderSms(request.POST)

        if send.is_valid():

            send.save()
            i =  Rdv.objects.get('-id')
            telnyx.Message.create(from_=your_telnyx_number,to=destination_number,text="Rendez Vous Resver Le {} A {} | Client {} | Service {} | Genre {} | Tel {} | Email {}".format(i.date, i.heure, i.nom, i.service, i.genre, i.tele, i.email),)
            redirect('/')
                



    else:
        send = senderSms()



    context = {
        'form': send
    }

    return render(request, 'home.html', context)


def sender(request):

    if request.method == 'POST':

        send = senderSms(request.POST)

        if send.is_valid():

            send.save()
            i =  Rdv.objects.get('-id')
            telnyx.Message.create(from_=your_telnyx_number,to=destination_number,text="Rendez Vous Resver Le {} A {} | Client {} | Service {} | Genre {} | Tel {} | Email {}".format(i.date, i.heure, i.nom, i.service, i.genre, i.tele, i.email),)
            redirect('/')
                



    else:
        send = senderSms()


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
def blogForm(request):
    
    context = {

    }

    return render(request, 'admin/addblog.html', context)

def logoutPage(request):
    
    logout(request)
    return redirect('/login')