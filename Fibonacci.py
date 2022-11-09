def fibonacci(x, r):
    res = [0, 1]
    for i in range(r-2):
        res.append(res[-1] + res[-2])
    return res

print(fibonacci(0, 15))