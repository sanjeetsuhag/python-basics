# Get a number from user input
n = int(input('Enter a number: '))

print(f'\nNumbers < {n} with more than 3 prime factors:')

# Iterate through all numbers from 1 to n
for i in range(1, n):
    prime_factor_count = 0
    # For the currently selected number, iterate through all its possible factors
    for j in range(2, int(i / 2) + 1):
        # If a factor is found, check if it's a prime
        # If it is a prime, increment the prime count for the currently selected number
        # If the prime count is greater than 3, print the currently selected number
        if i % j == 0:
            is_prime = True
            for k in range(2, int(j / 2) + 1):
                if j % k == 0:
                    is_prime = False
            if is_prime == True:
                prime_factor_count = prime_factor_count + 1
    if prime_factor_count > 3:
        print(i)10