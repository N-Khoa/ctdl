def neper(n):
    result = 0
    factorial = 1
    for k in range(n + 1):
        result += 1 / factorial
        factorial *= (k + 1)
    return result
