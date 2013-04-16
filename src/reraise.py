import inspect
import sys


def reraise_as(new_exception):
    """
    >>> try:
    >>>     do_something_crazy()
    >>> except Exception:
    >>>     reraise_as(UnhandledException)
    """
    __traceback_hide__ = True  # NOQA

    e_type, e_value, e_traceback = sys.exc_info()

    if inspect.isclass(new_exception):
        new_exception = new_exception()

    new_exception.__cause__ = e_value

    raise type(new_exception), new_exception, e_traceback
