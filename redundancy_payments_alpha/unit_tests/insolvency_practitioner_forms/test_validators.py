import unittest
from ...insolvency_practitioner_forms.forms.validators import validators
from wtforms import Form
from wtforms.validators import ValidationError


class FakeField():
    data = 'wibble'


class FakeForm():
    field_to_validate = FakeField()


class TestDateValidator(unittest.TestCase):
    def test_date_validator_raises_validation_error(self):
        form = FakeForm()
        self.assertRaises(
            ValidationError,
            validators.parses_to_date,
            form,
            form.field_to_validate
        )

