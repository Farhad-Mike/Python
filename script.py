import logging, os, tempfile, functools


if __debug__:
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.path.join(tempfile.gettempdir(), "logged.log"))
    logger.addHandler(handler)
    def logged(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            log = "called: " + function.__name__ + "("
            log += ", ".join(["{0!r}".format(a) for a in args] + ["{0!s}={1!r}".format(k, v) for k, v in kwargs.items()])
            result = exception = None
            try:
                result = function(*args, **kwargs)
                return result
            except Exception as err:
                exception = err
            finally:
                log += ((") -> " + str(result)) if exception is None else ") {0}: {1}".format(type(exception), exception))
            logger.debug(log)
            if exception is not None:
                raise exception
            return wrapper
else:
    def logged(function):
        return function

@logged
def discounted_price(price, percentage, make_integer=False):
    result = price * ((100 - percentage) / 100)
    if not (0 < result <= price):
        raise ValueError("invalid price")
    return result if not make_integer else int(round(result))


