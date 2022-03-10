from .validators import (
    validate_check_in,
    validate_check_out,
    validate_current_year,
    validate_gte_zero,
    validate_guests,
    validate_phone,
)

import uuid
from django.db import models
from django.core.validators import validate_email
from django.utils import timezone
from djmoney.models.fields import MoneyField


class RoomType(models.Model):
    """
    Tipo de habitación.

    En la base de datos inicial tenemos:
    Individuales, dobles, triples, y familiares (cuádruples)
    """

    name = models.CharField(max_length=24, blank=False, null=False)
    max_capacity = models.IntegerField(
        validators=[validate_guests], blank=False, null=False
    )
    price_per_night = MoneyField(
        validators=[validate_gte_zero],
        decimal_places=2,
        default=0,
        default_currency="EUR",
        max_digits=11,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class Room(models.Model):
    """
    Habitación.

    Su número es la clave primaria auto-incremental.
    Se pudiera representar en formato 001.
    Una habitación debe ser de un tipo.
    """

    number = models.AutoField(primary_key=True)
    room_type = models.ForeignKey(
        RoomType, on_delete=models.PROTECT, blank=False, null=False
    )

    def __str__(self):
        return f"#{self.number}, {self.room_type.name}"


class Reservation(models.Model):
    """
    Reserva.

    El localizador es un UUID, actuando como clave primaria.
    Inicialmente hice un modelo Cliente pero como no se asume que un cliente
    puede hacer varias reservas, no es necesario conservar la identidad.

    El campo valid funciona para deshabilitar reservas, lo que puede ser útil
    para no considerarlas pero sin borrarlas.
    Su funcionalidad está por implementarse.
    """

    locator = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact_name = models.CharField(max_length=254, blank=False, null=False)
    email = models.EmailField(
        validators=[validate_email], max_length=254, blank=False, null=False
    )
    phone_number = models.CharField(
        validators=[validate_phone], max_length=17, blank=False, null=False
    )
    check_in = models.DateField(
        default=timezone.now,
        validators=[validate_check_in, validate_current_year],
        blank=False,
        null=False,
    )
    check_out = models.DateField(
        default=timezone.now,
        validators=[validate_check_out, validate_current_year],
        blank=False,
        null=False,
    )
    num_guests = (
        models.IntegerField(
            default=1, validators=[validate_guests], blank=False, null=False
        ),
    )
    cost = MoneyField(
        validators=[validate_gte_zero],
        decimal_places=2,
        default=0,
        default_currency="EUR",
        max_digits=11,
        blank=False,
        null=False,
    )

    room = models.ForeignKey(Room, on_delete=models.PROTECT, blank=False, null=False)
    valid = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return str(self.locator)[:7]
