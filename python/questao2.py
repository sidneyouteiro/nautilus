def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def questao2(n):
    if n < 2:
        return -1
    m = 2
    for i in range(2,n+1):
        if n % i == 0:
            if is_prime(i):
                m = i
    return m

