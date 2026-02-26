def zeros(n):
    res = []
    for i in range (1, n):
        if 5**i > n: 
            return sum(res)
        res.append(n // (5**i))
    return sum(res)