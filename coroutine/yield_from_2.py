def func():
    """生成器函数"""
    n = 0
    while True:
        s = yield n
        print('sss: {}'.format(s))
        if s is None:
            break
        n += 1
    return n


def deligate():
    """委派生成器"""
    result = yield from func()
    print('the result is: {}'.format(result))


def main():
    """调用"""
    g = deligate()
    print(next(g))  # 0
    for i in range(3):
        print(g.send(i))  # the result is 3
    try:
        g.send(None)
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
