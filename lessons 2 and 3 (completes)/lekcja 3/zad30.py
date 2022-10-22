def isPrime(n):
    i = 2
    if i == 1:
        return False
    while i < n:
        if n%i == 0:
            return False
        i += 1
    return True

n = int(input("Ill tell you if this number is prime "))
print(isPrime(n))