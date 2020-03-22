# Accept a number n from the user
n = int(input('Enter a number: '))
# Print table header
print(f'\nDescending Count from {n} to {1}:')
# Run a loop from 1 to n.
for i in range(n):
    # Calculate number
    p = n - i
    # Print number
    print(f'{p}')
