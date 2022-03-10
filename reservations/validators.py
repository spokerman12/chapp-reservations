import re

from datetime import timedelta, datetime

from django.core.exceptions import ValidationError

TODAY = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
TOMORROW = TODAY + timedelta(days=1)


def convert_dt(date_str):
    """
    Convierte una fecha "%Y-%m-%d" en datetime.date
    """
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def validate_gte_zero(value):
    """
    Verifica que value >= 0
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
    Verifica que value no sea en el pasado
    """
    if type(value) == str:
        value = convert_dt(value)
    if value < TODAY:
        raise ValidationError(
            f"Check-in date {value} must be at least today.",
        )


def validate_check_out(value):
    """
    Verifica que value sea al menos mañana
    """
    if type(value) == str:
        value = convert_dt(value)
    if value < TOMORROW:
        raise ValidationError(
            f"Check-out date {value} must be at least tomorrow.",
        )


def validate_current_year(value):
    """
    Verifica que value sea en el año en curso
    """
    if type(value) == str:
        value = convert_dt(value).year
    if value != datetime.today().year:
        raise ValidationError(
            f"Please select a date in {datetime.today().year}",
        )


def validate_check_in_out(check_in, check_out):
    """
    Verifica que check_in sea antes que check_out
    """

    if type(check_in) == str:
        check_in = convert_dt(check_in)
    if type(check_out) == str:
        check_out = convert_dt(check_out)

    if check_in >= check_out:
        raise ValidationError(
            f"Check-In date {check_in} cannot be after Check-Out date {check_out}",
        )


def validate_phone(value):
    """
    Verifica que value tenga formato de número telefónico
    """
    if not re.match(r"^\+?1?\d{9,15}$", value):
        raise ValidationError("Format:'+999999999'. Up to 15 digits allowed.")


def validate_guests(value):
    """
    Verifica que value esté entre 1 y 4 (asumiendo que no tendremos habitaciones
    más grandes por lo pronto)
    """
    if not (1 <= value <= 4):
        raise ValidationError(
            f"Our rooms only accomodate between 1 to 4 guests",
        )
