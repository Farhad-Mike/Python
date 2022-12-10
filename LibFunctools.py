import functools

# Set fixed arguments in function
def multiply(x, y):
    return x * y
dpl = functools.partial(multiply, 2)
print(dbl(4))


