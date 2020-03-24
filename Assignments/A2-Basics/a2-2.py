n = int(input('Enter a number: '))

fib_1 = 0
fib_2 = 1

print(f'\nFibonacci Sequence to {n} terms:')
print(fib_1)
print(fib_2)
for i in range(3, n):
    fib_i = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = fib_i
    print(fib_i)
    