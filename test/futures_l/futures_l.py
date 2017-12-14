
# # -*- coding:utf-8 -*-

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def test(num):
    import time
    time.sleep(10)
    return time.ctime(), num
 

def is_prime(n):
    if n % 2 == 0:
        return False
    sleep(10)
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True



# with concurrent.futures.ProcessPoolExecutor() as executor:
#     print(executor.map(is_prime, PRIMES))
#     for i in executor.map(is_prime, PRIMES):
#         print(i)
#     for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#         print('%d is prime: %s' % (number, prime))
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

future1 = executor.submit(test, 1)
# print(future1)
print future1.result()
print("😁😁😁😁😁😁😁😁😁😁😁😁😁")
