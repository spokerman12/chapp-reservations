import uuid
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from djmoney.models.fields import MoneyField


class RoomType(models.Model):
    name = models.CharField(max_length=24)
    max_capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    price_per_night = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='EUR',
        max_digits=11,
    )

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.AutoField(primary_key=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT)

    def __str__(self):
        return f"#{self.number}, {self.room_type}"

class Reservation(models.Model):

    def validate_date(self, date):
        if date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

    locator = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    check_in = models.DateField(default=timezone.now, validators=[validate_date])
    check_out = models.DateField(default=timezone.now, validators=[validate_date])
    num_guests = models.IntegerField()
    cost = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='EUR',
        max_digits=11,
    )
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.locator[:7]

class Client(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False)
    email = models.CharField(validators=[EmailValidator()], max_length=254, blank=False, null=False)
    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must look like +999999999")
    phone_number = models.CharField(validators=[phone_validator], max_length=17, blank=False, null=False)

    def __str__(self):
        return self.name
