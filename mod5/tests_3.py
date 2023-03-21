import unittest

from app_3 import BlockErrors


class TestExceptionStub(unittest.TestCase):
    def test_ignore_error():
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / 0
        print('Executed without errors')

    def test_raise_error():
        err_types = {ZeroDivisionError}
        with pytest.raises(TypeError):
            with BlockErrors(err_types):
                a = 1 / '0'
        print('Executed without errors')

    def test_ignore_inner_error():
        outer_err_types = {TypeError}
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with BlockErrors(inner_err_types):
                a = 1 / '0'
            print('Internal block: executed without errors')
        print('Outer block: no errors')

    def test_ignore_sub_error():
        err_types = {Exception}
        with BlockErrors(err_types):
            try:
                a = 1 / '0'
            except TypeError:
                pass
            print('Executed without errors')
