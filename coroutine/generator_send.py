def generator():
    s = yield "hello"
    print('输入值为:{}'.format(s))
    yield s


gen = generator()
print(next(gen))
print(gen.send("world"))
