def genrange(start: int, end: int):
    i = start
    n = end
    while i <= n:
        yield i
        i += 1

print(list(genrange(1, 10)))
