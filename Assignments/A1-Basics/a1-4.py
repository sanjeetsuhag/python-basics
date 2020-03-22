# Accept a number n from the user
n = int(input('Enter a number: '))
# Factor count
factor_count = 0
# Run a loop from 1 to n - 1.
for i in range(1, n):
    # Check if it's a factor
    if n % i == 0:
        # Increment factor count
        factor_count = factor_count + 1
# Check if it's prime
if factor_count > 1:
    print(f'{n} is not prime number.')
else:
    print(f'{n} is a prime number.')