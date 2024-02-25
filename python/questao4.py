from python.questao2 import is_prime
def questao4():
    s = 0
    for i in range(1000):
        if is_prime(i):
            s += i
    return s

