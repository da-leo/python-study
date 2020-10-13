def func():
    for x in 'ABC':
        yield x


for x in func():
    print(x)


def func2():
    yield from 'ABC'


for x in func2():
    print(x)

