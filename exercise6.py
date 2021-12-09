def prime(n):
    is_prime = True
    if n == 1:
        return False
    else:
        for i in range(2, (int)(n//2)+1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime 

P = []
for i in range (2, 1000):
    if prime(i):
        P.append(i)

print (P)
