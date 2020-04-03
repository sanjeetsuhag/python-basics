# Assignment 3 - Python Basics

## Notes

### Taking Input from the User

To accept input from a user at runtime, we use the `input` function:

```
number = int(input('Enter your number: '))
string = input('Enter your string: ')
```

### Printing Output to the User

To print output to the user, we use the `print` function.

```
print('This is a message without a variable')

n = 100
print(f'This is a message with a variable! The variable value of n is {n}')

print('\nThis message prints a new line before its message')
```

### Looping to a Range

To loop over a range of numbers, we use the `range` function with a `for` loop:

```
for i in range(1, 11):
    print('This message will print 10 times')
    print(f'It is currently on loop number {i}')

n = 5
for i in range(1, n + 1):
    print(f'This message will print {n + 1} times')
    print(f'It is currently on loop number {i}')
```

### Checking for Equality between Values

To check if two values are equal, we use the `==` operator:

```
n = 2
if n == 2:
    print(f'{n} is equal to 2!')
else:
    print(f'{n} is not equal to 2!')


code = 'Sam'
if code == 'Sam':
    print(f'{code} is equal to Sam!')
elif code == '😎':
    print(f'{code} is equal to 😎!')
else:
    print(f'{code} is not equal to Sam or 😎')

```

> Hint: You can use emojis inside strings, just like you use other alphabets inside string. To type emojis on a Mac, press `Command(⌘) + Control(⌃) + Space`.

---

## Problems

1. Write a Python script to accept a number from a user and check if it is even or odd. The output should look exactly as given below:

```
Enter a number: 76

76 is an even number.
```

```
Enter a number: 75

75 is an odd number.
```

---

2. Write a Python script to accept a number `a` and a number `b` from a user and check if `b` is a factor of `a`. The output should look exactly as given below:

```
Enter the first number: 4
Enter the second number: 2

2 is a factor of 4.
```

```
Enter the first number: 4
Enter the second number: 3

3 is not a factor of 4.
```

---

3. Write a Python script to accept a number `n` from a user and print all numbers from `1` to `n`. The output should look exactly as given below:

```
Enter a number: 5

All numbers from 1 to 5 are: 
1
2
3
4
5
```

---

4. Write a Python script to accept a number `n` and print all numbers divisible by 3 from `1` to `n`. The output should look exactly as given below:

```
Enter a number: 19

All numbers from 1 to 19 divisible by 3 are: 
3
6
9
12
15
18
```

---

5. Write a Python script to accept a number `a` and a number `b` from a user and print which of the two is the greater number or if they are equal. The output should look exactly as given below:

```
Enter the first number: 3
Enter the second number: 4

4 is bigger than 3.
```

```
Enter the first number: 4
Enter the second number: 4

4 is equal to 4.
```

---

**Little Assignment**

6. Write a program a Python script to accept a string `stuffie` from a user and print out its corresponding emoji. You are only required to provide emojis for the following strings: `Purdue Puppy`, `Raccoon`, `Elephant` or `Leopard`. The output should look exactly as given below:

```
Enter the stuffie name: Purdue Puppy

🐕
```

```
Enter the stuffie name: Elephant

🐘
```

```
Enter the stuffie name: Bear

I do not have that stuffie yet 😭
```