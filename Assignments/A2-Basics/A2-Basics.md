# Assignment 2 - Python Basics

## Notes

#### Conditionals

You can use conditionals to check for certain conditions in Python. The syntax is illustrated in the following example:

```
# Check if n is divisible by 2 or 3 or neither.
n = input('Enter a number: ')
if n % 2 == 0:
   print('2 is a factor!')
elif n % 3 == 0:
   print('3 is a factor!)
else:
   print('2 and 3 are not factors!')
```

You can even nest conditional statements. The syntax is illustrated in the following example:
```
# Check if correct username and password are supplied.
username = input('Enter username: ')
password = input('Enter password: ')

correct_username = 'sam'
correct_password = 'puff'

if username == correct_username:
   if password == correct_password:
      print('Logged In')
   else:
      print('Incorrect Password')
else:
   print('Invalid User')
```

#### For Loops

You can use a `for` loop in conjunction with the `range` function to iterate over a numerical sequence. The syntax is illustrated in the following example:

```
# Iterate i through 0 to n - 1
for i in range(n):
   print(i)
```

You can also nest loops within each other. You will be required to do that for this assignment. The syntax is illustrated in the following example:

```
# One nested loop

n = 3
# Iterate i through 1 to n
for i in range(1, n + 1):
   # Iterate j through 1 to n
   for j in range(1, n + 1):
      print(f'i = {i}, j = {j}')
```

```
# Two nested loops

n = 3
# Iterate i through 1 to n
for i in range(1, n + 1):
   # Iterate j through 1 to i
   for j in range(1, i + 1):
      # Iterate k through 1 to j
      for k in range(1, j + 1):
         print(f'i = {i}, j = {j}, k = {k}')
```

```
# Nested loop example to print number of factors for all numbers from 2 to n.

# Iterate through all numbers from 2 to n.
for i in range(2, n + 1):
   # Reset factor count for each i.
   factor_count = 0
   # Iterate through all numbers from 1 to i / 2 (all it's possible factors).
   for j in range(1, int(i / 2) + 1):
      # Check if j is a factor of i.
      if i % j == 0:
         # Increase the factor count for i.
         factor_count = factor_count + 1
   # Print factor count for i.
   print(f'{i} has {factor_count} factor(s).')
```


> Note: Try to run these blocks of code in Python. See how the loops execute when they are nested; the print statements are set to print out the values of the iterated variables (`i`, `j`, `k` - Keep in mind, these variables names are arbitrary.) Simply copy a block of code in a file (must have the extension `.py`) and run on the Terminal, using `python3 <your_file_here>.py`

---

## Problems

1. Write a Python script to accept a number from a user and calculate its factorial. The factorial of a number `n` is the product of all positive integers less than or equal to n.

   ```
   Enter a number: 6

   Factorial of 6 = 720
   ```

---

2. Write a Python script to accept a number `n` from a user and print the Fibonnaci sequence to the first `n` terms. The Fibonacci sequence is the sequence of numbers such that each number is the sum of the two preceding ones, starting from 0 and 1. You may assume that `n` will always be greater than 2. The output should look exactly as given below:

   ```
   Enter a number: 8

   Fibonacci Sequence to 8 terms:
   0
   1
   1
   2
   3
   5
   8
   13
   ```

---

3. Write a Python script to accept a number from a user and print out all its prime factors. The output should look exactly as given below:

   ```
   Enter a number: 75

   Prime Factors of 75:
   3
   5
   ```

---

4. Write a Python script to accept a number `n` from a user and print all Perfect numbers less than `n`. A Perfect number is a number whose factors all add up to give the same number. For example, `6` is a Perfect number since its factors are `1, 2, 3` and `1 + 2 + 3 = 6`. The output should look exactly as given below:

   ```
   Enter a number: 1000

   Perfect Numbers < 1000:
   6
   28
   496
   ```

---

**Extra Credit**

5. Write a Python script to accept a number `n` from a user and print all numbers less than `n` that have more than 3 prime factors. The output should look exactly as given below:

   ```
   Enter a number: 500

   Numbers < 500 with more than 3 prime factors:
   210
   330
   390
   420
   462
   ```