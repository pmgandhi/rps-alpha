import unittest
from hamcrest import *


class TestTestsWork(unittest.TestCase):
    def test_some_simple_asserts(self):
        expected = "Hello, World!"
        actual = ", ".join(["Hello", "World!"])
        assert_that(actual, equal_to(expected))
