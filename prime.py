import math
import datetime


def get_the_primes(n):
    true_primes = (n) * [True]
    prime_list = []
    for i in range(2, int(math.sqrt(n))):
        for j in range(i*i, n, i):
            true_primes[j] = False

    for i in range(2, n):
        if true_primes[i]:
            prime_list.append(i)
    return prime_list


def get_the_primes_fast(m):
    possible_primes = (m) * [0]
    primes = []
    for i in range(2, int(math.sqrt(m))):
        for j in range(i*i, m, i):
            possible_primes[j] = 1

    for i in range(2, len(possible_primes)):
        if possible_primes[i] == 0:
            primes.append(i)
    return primes


def main():
    n = int(input("Please give me a number: "))
    before = datetime.datetime.now()
    print(get_the_primes(n))
    after = datetime.datetime.now()
    print((after-before).total_seconds())
    m = int(input("please give me another one: "))
    before1 = datetime.datetime.now()
    print(get_the_primes_fast(m))
    after1 = datetime.datetime.now()
    print((after1-before1).total_seconds())


if __name__ == '__main__':
    main()
