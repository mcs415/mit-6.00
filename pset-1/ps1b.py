from math import log

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True

def product(n):
    sum = 0.0
    for i in range(2,n):
        if is_prime(i):
            sum += log(i)
    print sum, n, sum/n


trials = [5,7,956,78,98,1454,3412,6789,23124]

for trial in trials:
	answer = product(trial)
