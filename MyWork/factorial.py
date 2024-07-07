def fact(n):
    result = 1
    for x in range(2, n+1):
        result *= x
    return result

def rfact(n):
    if n == 1:
        return 1
    else:
        return n * rfact(n-1)