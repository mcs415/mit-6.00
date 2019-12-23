#PROBLEM SET 1
#Morgan Sippel
#4:18 AM Dec. 14, 2019

def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
            break
    return True

def nth_prime(x):
    #start at three to avoid confusion
    num = 3
    #prime number count, starting at 3 = 2, 3.  1 suprisingly isnot prime
    prime = 2
    while prime < x:
        num += 2
        if prime_number(num):
            prime += 1
    return num

print(nth_prime(1000))
