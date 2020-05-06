def print_primes(n):
    primes = [2, 3]
    for i in range(5, n, 2):
        for j in range(3, int(i ** 0.5)+1, 2):
            if i % j == 0:
                break
        else:
            primes.append(i)

    print(primes)

print_primes(100000)