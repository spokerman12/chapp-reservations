from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path("", include("reservations.urls")),
    path("admin/", admin.site.urls),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)  # type: ignore

# Para poder imprimir los mensajes de error
# puedo hacer override de las paginas
handler404 = 'reservations.views.error_404_view'
handler500 = 'reservations.views.error_500_view'
handler400 = 'reservations.views.error_400_view'
