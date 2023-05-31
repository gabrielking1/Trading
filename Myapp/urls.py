from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,  name='index'), 
    path('dashboard/<int:id>', views.dashboard, name = 'dashboard'),
    path('check/', views.check, name = 'check'),

    path('Trader-admin/', views.admin, name = 'admin')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)