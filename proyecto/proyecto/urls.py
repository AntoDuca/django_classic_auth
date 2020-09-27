from django.contrib import admin
from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    # Sección para usuarios
    path('', views.welcome),
    path('register', views.register), 
    path('login', views.login),
    path('logout', views.logout),

    path('admin/', admin.site.urls),

    #Autenticacion con facebook
    path('oauth/', include('social_django.urls', namespace='social'))
]
