from django.core.exceptions import ValidationError
from ..validators import (
    validate_gte_zero,
    validate_check_in,
    validate_check_out,
    validate_current_year,
    validate_check_in_out,
    validate_phone,
    validate_guests,
)

from datetime import datetime

from django.test import TestCase


class TestValidators(TestCase):
    def test_validate_gte_zero(self):
        with self.assertRaises(ValidationError):
            validate_gte_zero(-1)
        validate_gte_zero(0)
        validate_gte_zero(1)

    def test_validate_check_in(self):
        with self.assertRaises(ValidationError):
            validate_check_in("2022-01-01")
        validate_check_in("2022-12-01")
        validate_check_in(datetime.today().strftime("%Y-%m-%d"))


# def test_validate_check_in(value):

# def test_validate_check_out(value):

# def test_validate_current_year(value):

# def test_validate_check_in_out(check_in, check_out):

# def test_validate_phone(value):

# def test_validate_guests(value):
