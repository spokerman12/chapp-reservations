from wsgiref.validate import validator
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
    number = models.AutoField(primary_key=True)
    room_type = models.ForeignKey(
        RoomType, on_delete=models.PROTECT, blank=False, null=False
    )

    def __str__(self):
        return f"#{self.number}, {self.room_type.name}"


class Reservation(models.Model):

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
