def calculate(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculate, numbers)
print(result)
print(list(result))
