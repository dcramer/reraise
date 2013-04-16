from unittest import TestCase
from reraise import reraise_as


def an_error():
    raise NotImplementedError('foo bar')


class ReraiseAsTest(TestCase):
    def test_simple_without_value(self):
        try:
            try:
                an_error()
            except NotImplementedError as orig_exc:
                reraise_as(ValueError)
            else:
                self.fail('NotImplementedError was not raised')
        except ValueError as exc:
            assert exc.message == 'foo bar'
            assert exc.__cause__ == orig_exc
        else:
            self.fail('ValueError was not re-raised')

    def test_simple_with_value(self):
        try:
            try:
                an_error()
            except NotImplementedError as orig_exc:
                reraise_as(ValueError('biz baz'))
            else:
                self.fail('NotImplementedError was not raised')
        except ValueError as exc:
            assert exc.message == ''
            assert exc.__cause__ == orig_exc
        else:
            self.fail('ValueError was not re-raised')
