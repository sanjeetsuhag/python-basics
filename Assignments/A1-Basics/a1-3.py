# Accept a number n from the user
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
# Determine the smaller number
smaller = n1
if (n2 < n1):
    smaller = n2
# Give HCF a value of 1 (since 1 is a common factor to all numbers)
hcf = 1
# Run a loop from 1 to n - 1.
for i in range(1, smaller + 1):
    # Check if both numbers are divisible by i and if i is greater than the current HCF
    if n1 % i == 0 and n2 % i == 0 and i > hcf:
        hcf = i
print(f'\nHighest Common Factor of {n1} and {n2} is {hcf}')