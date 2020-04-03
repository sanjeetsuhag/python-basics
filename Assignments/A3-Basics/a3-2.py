a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

if a % b == 0:
    print(f'\n{b} is a factor of {a}.')
else:
    print(f'\n{b} is not a factor of {a}.')