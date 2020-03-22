# Accept a number n from the user
n = int(input('Enter a number: '))
# Print table header
print(f'\nFactors of {n}:')
# Run a loop from 1 to n - 1.
for i in range(1, n):
    # Check if it's a factor
    if n % i == 0:
        # Print multiplication table entry
        print(f'{i}')
