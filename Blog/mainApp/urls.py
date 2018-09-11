from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    #path('contact/' , views.contact , name='contact'),
   # path('login/' , views.log_in , name="login"),
   # path('accounts/', include('django.contrib.auth.urls')),
    path('MkNews/' , views.makeNews, name="mk") ,


    #path('article/', views.article, name="art"),
]
