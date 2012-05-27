# # A perfect number is a number for which the sum of its proper divisors is
# # exactly equal to the number. For example, the sum of the proper divisors of 28
# # would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# # A number n is called deficient if the sum of its proper divisors is less than
# # n and it is called abundant if this sum exceeds n.
# # As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# # number that can be written as the sum of two abundant numbers is 24. By
# # mathematical analysis, it can be shown that all integers greater than 28123
# # can be written as the sum of two abundant numbers. However, this upper limit
# # cannot be reduced any further by analysis even though it is known that the
# # greatest number that cannot be expressed as the sum of two abundant numbers is
# # less than this limit.
# # Find the sum of all the positive integers which cannot be written as the sum
# # of two abundant numbers.

from math import sqrt

import prime

def prob23():
    limit = 20162
    s = 0
    abn = set()
    prime_sieve = prime.prime_table(limit)
    for n in range(1, limit):
        if is_abundant(n, prime_sieve):
            abn.add(n)
        if not any((n-a in abn) for a in abn):
            s += n
    return s

def is_abundant(n, prime_sieve):
    if (n % 2 == 1 and n > 2 and n < len(prime_sieve) and prime_sieve[int((n-1)/2)] == True):
        return False
    if n %2 != 0 and n % 3 != 0 and n < 5391411025:
        return False
    return n < sum_of_divisors(n)

def sum_of_divisors_a(n):
    prod = 1
    k = 2
    while (k*k <= n):
        p = 1
        while(n%k==0):
            p=p*k+1
            n/=k
        prod*=p
        k += 1

    if(n>1):
        prod*=1+n
    return prod

def sum_of_divisors(n):
    sum_divisors = 1
    i = 2
    while (i*i <= n):
        if (n % i == 0):
            sum_divisors += i
            if (i*i != n):
                sum_divisors += int(n/i)
        i += 1
    return sum_divisors

import time
s = time.time()
print(sum_of_divisors_a(6))
print(time.time()-s)