from . import views
from django.views.static import serve

from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path

urlpatterns = [
    path('', include('reservations.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
