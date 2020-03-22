# Accept a number n from the user
n = int(input('Enter a number: '))
# Print table header
print(f'\nMultiplication Table for {n}:')
# Run a loop from 1 to 10.
for i in range(1, 11):
    # Calculate mulitple
    p = (n * i)
    # Print multiplication table entry
    print(f'{n}x{i}={p}')
