import re

from datetime import timedelta, datetime

from django.core.exceptions import ValidationError

TODAY = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
TOMORROW = TODAY + timedelta(days=1)


def validate_gte_zero(value):
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
    if datetime.strptime(value, "%Y-%m-%d") < TODAY:
        raise ValidationError(
            f"Check-in date {value} must be at least today.",
        )


def validate_check_out(value):

    # Nota
    if datetime.strptime(value, "%Y-%m-%d") < TOMORROW:
        raise ValidationError(
            f"Check-out date {value} must be at least tomorrow.",
        )


def validate_current_year(value):
    if datetime.strptime(value, "%Y-%m-%d").year != datetime.today().year:
        raise ValidationError(
            f"Please select a date in {datetime.today().year}",
        )


def validate_check_in_out(check_in, check_out):

    # Nota
    if datetime.strptime(check_in, "%Y-%m-%d") >= datetime.strptime(
        check_out, "%Y-%m-%d"
    ):
        raise ValidationError(
            f"Check-In date {check_in} cannot be after Check-Out date {check_out}",
        )


def validate_phone(value):
    if not re.match(r"^\+?1?\d{9,15}$", value):
        raise ValidationError("Format:'+999999999'. Up to 15 digits allowed.")


def validate_guests(value):

    # Nota
    if not (1 <= value <= 4):
        raise ValidationError(
            f"Our rooms only accomodate between 1 to 4 guests",
        )
