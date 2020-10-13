def generator():
    n = 0
    y = 0
    while True:
        y += 1
        print('xian')
        yield n, y
        y += 10
        print('hou')
        n += 1


gen = generator()
print(gen)  # 生成器对象

for i in range(100):
    print(next(gen))  # 0 - 99


