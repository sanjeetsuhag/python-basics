n = int(input('Enter a number: '))

print(f'\nPerfect Numbers < {n}:')

for i in range(1, n):
    factor_sum = 0
    for j in range(1, int(i / 2) + 1):
        if i % j == 0:
            factor_sum = factor_sum + j
    if factor_sum == i:
        print(i)