a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

if a > b:
    print(f'\n{a} is bigger than {b}.')
elif b > a:
    print(f'\n{b} is bigger than {a}.')
else:
    print(f'\n{a} is equal to {b}.')