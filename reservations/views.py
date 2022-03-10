from django.forms import ValidationError
from reservations.models import Reservation
from .utils import get_offers, overlapping_reservations

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import sys


class Index(TemplateView):
    """
    Vista principal para iniciar el proceso
    de reserva
    """
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class Offers(TemplateView):
    """
    Vista donde se muestran las
    posibilidades de reserva
    """
    template_name = "offers.html"

    def post(self, request):

        offers = get_offers(
            check_in=request.POST["check_in"],
            check_out=request.POST["check_out"],
            num_guests=request.POST["num_guests"],
        )

        return render(
            request,
            self.template_name,
            {
                "offers": offers,
                "num_offers": len(offers),
                "check_in": request.POST["check_in"],
                "check_out": request.POST["check_out"],
                "num_guests": request.POST["num_guests"],
            },
        )

    def get(self, _):
        return redirect("index")


class Confirm(TemplateView):
    """
    Vista donde se provee la información
    de contacto para confirmar la reserva
    """
    template_name = "confirm.html"

    def post(self, request):
        booking = {
            "room_number": request.POST["room_number"],
            "num_guests": request.POST["num_guests"],
            "full_price": request.POST["full_price"],
            "check_in": request.POST["check_in"],
            "check_out": request.POST["check_out"],
        }
        return render(request, self.template_name, booking)

    def get(self, _):
        return redirect("index")


class Success(TemplateView):
    """
    Vista donde se muestra el número localizador
    de la reserva
    """
    template_name = "success.html"

    def post(self, request):

        # Verifica que no haya reservas que solapen.
        # Esto debería confirmarse solo una vez,
        # pero por motivos prácticos se ejecuta de
        # esta forma.
        if overlapping_reservations(
            room_id=request.POST["room_number"],
            check_in=request.POST["check_in"],
            check_out=request.POST["check_out"],
        ):
            raise ValidationError(
                "The room is already reserved for the set time range. "
                "Please choose a different time range"
            )
        locator = Reservation.objects.create(
            room_id=request.POST["room_number"],
            num_guests=request.POST["num_guests"],
            cost=request.POST["full_price"],
            check_in=request.POST["check_in"],
            check_out=request.POST["check_out"],
            contact_name=request.POST["contact_name"],
            email=request.POST["email"],
            phone_number=request.POST["phone"],
            valid=True,
        )

        return render(request, self.template_name, {"locator": str(locator)})


class List(TemplateView):
    """
    Vista de listado de todas las
    reservas en el sistema
    """
    template_name = "list.html"

    def get(self, request):
        reservations = Reservation.objects.all()
        return render(request, self.template_name, {"reservations": reservations})


# Vistas para páginas de error

def error_404_view(request, *args, **argv):
    response = render(
        request,
        "custom_404.html",
    )
    response.status_code = 404
    return response


def error_500_view(request, *args, **argv):
    response = render(
        request,
        "custom_500.html",
        {"error_message": sys.exc_info()[1]},
    )
    response.status_code = 500
    return response


def error_400_view(request, *args, **argv):
    response = render(
        request,
        "custom_400.html",
    )
    response.status_code = 400
    return response
