def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_n_primes(count):
    primes, num = [], 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Вывод первых 20 простых чисел
primes = first_n_primes(20)
print(primes)