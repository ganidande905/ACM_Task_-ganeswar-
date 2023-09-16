import sys
t = int(input().strip())

if 1 <= t <= 10:
    for _ in range(t):
        n = int(input().strip())
        if 10 <= n <= 10**12:
            factors = []
            divisor = 2

            while divisor <= n:
                if n % divisor == 0:
                    factors.append(divisor)
                    n = n // divisor
                else:
                    divisor += 1

            if n > 1:
                factors.append(n)

            k = max(factors)  
            print(k)