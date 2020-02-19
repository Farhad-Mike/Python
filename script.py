import functools



def decorator_name(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() result isn't >= 0"
        return result
    return wrapper

@decorator_name
def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

print(discriminant(2, 2, 4))