from app.forms import senderSms
from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('hijama', hijama, name='hijama'),
    path('contact', contact, name='contact'),
    path('galerie', galerie, name='galerie'),
    path('send', sender, name='send'),
    path('dashboard', dashboard, name='dashboard'),
    path('blog', blog, name='blog'),
    path('addblog', blogFormer, name='addblog'),
    path('login', login, name='login'),
    path('logout', logoutPage, name='logout'),
]