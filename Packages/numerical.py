

# function to check if number is prime
def isCheck(n):
    flag = 1
    if n == 2:
        return True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            flag = 0
            return False
    if flag == 1:
        return True

# function to determine number of prime factors for a given number
def numberPrimeFactors(n):
    if isCheck(n):
        return 1
    count = 0
    for i in range(2, n//2 + 1):
        if isCheck(i) and n % i == 0:
            count = count + 1
    return count
