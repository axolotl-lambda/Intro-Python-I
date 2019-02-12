def isPrime(num):
    for x in range(2, num // 2):
        if num % x == 0:
            return False
    return True


print(isPrime(3))
print(isPrime(8))
print(isPrime(13))
print(isPrime(15))
print(isPrime(17))
