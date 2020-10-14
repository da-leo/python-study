from functools import wraps


def a_new_decorator(func):
    @wraps(func)
    def wrapTheFunction():
        print("i am doing some work before")
        func()
        print("i am doing some work after")
    return wrapTheFunction

def test_decorator_func():
    print('testing ...')



test_decorator_func()
a = a_new_decorator(test_decorator_func)
a()


# 进阶
@a_new_decorator
def test_decorator_func2():
    print('testing2 ...')


test_decorator_func2()

