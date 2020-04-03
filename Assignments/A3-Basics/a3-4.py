n = int(input('Enter a number: '))

print(f'\nAll numbers from 1 to {n} divisible by 3 are: ')
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)