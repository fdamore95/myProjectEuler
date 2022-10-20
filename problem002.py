n = 4000000

def fibonacci(n):
    first = 1
    second = 2
    new = first + second
    sum = second
    while new <= n:
        first = second
        second = new
        new = first + second
        if new % 2 == 0:
            sum += new
    return sum

print(fibonacci(n))
