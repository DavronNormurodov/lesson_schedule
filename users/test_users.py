from django.test import TestCase
import pytest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class TestClass:
    @pytest.mark.math
    def test_add(self, input_value):
        assert add(2, input_value) == 5

    @pytest.mark.parametrize("num, output", [(1, 4)])
    def test_subtract(self, num, output):
        assert subtract(5, num) == output
