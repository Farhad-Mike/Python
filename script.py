
def er():
    return ValueError

for _ in [1, 2, ValueError]:
    print(_)
    int(_)
    er()
else:
    print('done ')