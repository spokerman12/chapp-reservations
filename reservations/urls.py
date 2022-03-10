from . import views
from django.urls import path


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("offers", views.Offers.as_view(), name="offers"),
    path("confirm", views.Confirm.as_view(), name="confirm"),
    path("success", views.Success.as_view(), name="success"),
    path("list", views.List.as_view(), name="list"),
]
