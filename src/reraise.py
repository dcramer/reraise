import inspect
import sys


def reraise_as(new_exception_or_type):
    """
    >>> try:
    >>>     do_something_crazy()
    >>> except Exception:
    >>>     reraise_as(UnhandledException)
    """
    __traceback_hide__ = True  # NOQA

    e_type, e_value, e_traceback = sys.exc_info()

    if inspect.isclass(new_exception_or_type):
        new_type = new_exception_or_type
        new_exception = new_exception_or_type()
    else:
        new_type = type(new_exception_or_type)
        new_exception = new_exception_or_type

    new_exception.__cause__ = e_value

    raise new_type, new_exception, e_traceback
