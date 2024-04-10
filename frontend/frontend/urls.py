from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('thank/', views.thank, name='thank'),
    path('Categories/', views.categories, name='categories'),
    path('Opinion/', views.opinion, name='Opinion'),   
    path('acknowledgement/', views.thank, name='thankyou'),
    path('Electronics/', views.electronic, name='Electronics'),
    path('Movies/', views.movies_to_show, name='Movies'),
    path('Games/', views.game, name='game'),
    path('Vehicle/', views.vehicle, name='vehicle'),
    path("Categories/Movies/", views.movies_to_show, name='cat_movies'),
    path('Categories/Electronics/', views.electronic, name='electronic'),
    path('Categories/Games/', views.game, name='game'),
    path('Categories/Vehicle/', views.vehicle, name='vehicle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)