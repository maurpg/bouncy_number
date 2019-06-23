from unittest import TestCase
from .bouncy import evaluate_number , evaluate , is_bouncy

class BouncyTestCase(TestCase):
    """Class to relize test to functions of bouncy numbers"""
    def test_validate_input_bouncy(self):
        assert not evaluate_number('assfsfs')

    def test_validate_number_less_thah_0_and_more_that_100(self):
        assert not evaluate_number(200)

    def test_to_validate_that_numbers_is_positive(self):
        assert not evaluate_number(-3)


