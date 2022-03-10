import re

from datetime import timedelta, datetime

from django.core.exceptions import ValidationError

TODAY = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
TOMORROW = TODAY + timedelta(days=1)


def validate_gte_zero(value):
    """
    Valida que value >= 0
    """
    try:
        int(value)
    except Exception as e:
        if "Money" in str(e):
            value = value.amount
    if value < 0:
        raise ValidationError(
            f"{value} can't be negative",
        )


def validate_check_in(value):
    """
    Valida que value no sea en el pasado
    """
    if datetime.strptime(value, "%Y-%m-%d") < TODAY:
        raise ValidationError(
            f"Check-in date {value} must be at least today.",
        )


def validate_check_out(value):
    """
    Valida que value sea al menos mañana
    """
    if datetime.strptime(value, "%Y-%m-%d") < TOMORROW:
        raise ValidationError(
            f"Check-out date {value} must be at least tomorrow.",
        )


def validate_current_year(value):
    """
    Valida que value sea en el año en curso
    """
    if datetime.strptime(value, "%Y-%m-%d").year != datetime.today().year:
        raise ValidationError(
            f"Please select a date in {datetime.today().year}",
        )


def validate_check_in_out(check_in, check_out):
    """
    Valida que check_in sea antes que check_out
    """
    if datetime.strptime(check_in, "%Y-%m-%d") >= datetime.strptime(
        check_out, "%Y-%m-%d"
    ):
        raise ValidationError(
            f"Check-In date {check_in} cannot be after Check-Out date {check_out}",
        )


def validate_phone(value):
    """
    Valida que value tenga formato de número telefónico
    """
    if not re.match(r"^\+?1?\d{9,15}$", value):
        raise ValidationError("Format:'+999999999'. Up to 15 digits allowed.")


def validate_guests(value):
    """
    Valida que value esté entre 1 y 4 (asumiendo que no tendremos habitaciones
    más grandes por lo pronto)
    """
    if not (1 <= value <= 4):
        raise ValidationError(
            f"Our rooms only accomodate between 1 to 4 guests",
        )
