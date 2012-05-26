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
# import prime

# def prob23():
#     limit = 28123
#     prime_sieve = prime.prime_table(limit)
#     odd_abundant = []
#     even_abundant = []
#     non_abundant_sum = []

#     # Create an array of abundant numbers
#     for i in range(2, limit):
#         # A prime is not abundant
#         if (is_abundant(i, prime_sieve)):
#             if i % 2 == 0:
#                 even_abundant.append(i)
#             else:
#                 odd_abundant.append(i)

#     # Odd numbers that are the sums of 2 abundant numbers
#     for i in range(0, len(even_abundant)):
#         for j in range(0, len(odd_abundant)):
#             temp = even_abundant[i] + odd_abundant[j]
#             if temp < limit:
#                 non_abundant_sum.append(temp)
#     # Even number that are larger than 48 are the sums of 2 abundant numbers
#     for i in range(0, len(even_abundant)):
#         if ((i % 2 == 0) and (i > 48)) or (i in [24,30,32,36,38,40,42,44,48]):
#             non_abundant_sum.append(i)
#     non_abundant_sum = list(set(non_abundant_sum))

#     return sum(i for i in range(0, limit+1)) - sum(i for i in non_abundant_sum)

# def is_abundant(n, prime_sieve):
#     if (n % 2 == 1 and n > 2 and n < len(prime_sieve) and prime_sieve[int((n-1)/2)] == True):
#         return False
#     if n < 5391411025 and n %2 != 0 and n % 3 != 0:
#         return False

#     return n < sum_of_divisors(n)

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

# import time
# s = time.time()
# print(prob23() - 4179871)
# print(time.time()-s)

from math import sqrt

limit = 20162
s = 0
abn = set()
for n in range(1, limit):
  if sum_of_divisors(n) > n:
    abn.add(n)
  if not any( (n-a in abn) for a in abn ):
    s += n

print("Answer to PE23 = ", s)
