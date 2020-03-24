n = int(input('Enter a number: '))

print(f'\nPrime Factors of {n}:')

for i in range(2, n):
    if n % i == 0:
        is_prime = True
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime == True:
            print(i)