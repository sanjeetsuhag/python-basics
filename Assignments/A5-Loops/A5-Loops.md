# Assignment 5 - Loops

## Notes

### Loops

A loop allows a block of code to be executed repeatedly. A loop's execution is dependent on a condition. Whatever the condition for the loop is, as long as it holds `True`, it will keep executing the block of code inside the loop. In Python, loops can be created using `for` and `while` statements. 

A `while` is a more general purpose loop, that is dependent a `bool` condition.

![while loop](https://i.imgur.com/bpXLqBh.png)

A `for` loop is typically used in a numerical context, in conjunction with the `range` function.

![for loop](https://i.imgur.com/dhbuf7d.png)

> Note: Any loop that can be expressed in a `for` loop can also be expressed as `while` loop.

#### Examples

1. Write a loop in Python to print numbers from 1 to 10.

    Using a `for` loop:
    ```
    for i in range(1, 11):
        print(i)
    ```

    Using a `while` loop:
    ```
    i = 1
    while i <= 10:
        print(i)
        i = i + 1
    ```

2. Write a loop in Python to repeatedly ask the username for the magic word (`"Stuffie"`)

    ```
    word = input('Enter the magic word: ')
    while word != "Stuffie":
        print('Oops, that's wrong. Try again')
        word = input('Enter the magic word: ')
    print('Yay! That's correct!')
    ```

### Nested Loops

A loop can be nested inside another loop to create another level of repetition. There is no requirement for the loops being nested to be of the same kind. A `while` loop can be nested inside another `while` loop or a `for` loop. Similarly, a `for` loop can be nested inside a `for` or a `while` loop.

A `for` loop within a `for` loop would look like this:

![for loop inside for loop](https://i.imgur.com/UgNLP2G.png)

A `while` loop within a `while` loop would look like this:

![while loop inside while loop](https://i.imgur.com/mJihjKk.png)

A `while` loop within a `for` loop would look like this:

![while loop inside for loop](https://i.imgur.com/7dyHBST.pngb)

#### Examples

1. Write a loop to print all numbers from 1 to 10 and the sum of all numbers before it, next to each number.

    ```
    i = 1
    while i <= 10:
        sum = 0
        for j in range(1, i):
            sum = sum + j
        print(f'{i} - {sum}')
        i = i + 1
    ```

2. Write a program to print a triangle of stars (`*`) to `n` lines.

    ```
    n = int(input('No of lines: '))
    for i in range(n):
        output = ""
        for j in range(i, n + 1):
            output = output + " "
        for j in range(i + 1):
            output = output + "*"
        for k in range(1, i + 1):
            output = output + "*"
        print(output)
    ```


---

## Problems

1. Write a Python script to accept a number `n` from a user and create the following pattern:

    ```
    Enter n: 5
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ```

---

2. Write a Python script to accept a number `n` from a user and create the following pattern:

    ```
    Enter n: 7
    *     *
     *   *
      * *
       *
      * *
     *   *
    *     *
    ```
---

3. Write a Python script to accept a number `n` from a user, print all the numbers from 1 to `n`, and next to each number, print the sum of all the numbers up to it and the number of factors the sum has. The output should look exactly as given below:

   ```
    Enter n: 5
    1, Sum: 1, No. Of Factors of 1: 0
    2, Sum: 3, No. Of Factors of 3: 1
    3, Sum: 6, No. Of Factors of 6: 3
    4, Sum: 10, No. Of Factors of 10: 3
    5, Sum: 15, No. Of Factors of 15: 3
   ```

---

4. Write a Python script to create a guessing game. The game should have two phases, a setup phase and a play phase. First, in the setup phase, you will ask for the magic number and the maximum number of guesses a player can make. Then, in the playing phase, you will repeatedly ask the user to guess the number, telling them if they are too high or too low.

   ```
    SETUP PHASE

    Enter the magic number: 100
    Enter the maximum number of guesses: 4

    GAME PHASE

    Enter your guess: 50
    Too low! Try again.
    You have 3 guesses left.

    Enter your guess: 200
    Too high! Try again.
    You have 2 guesses left.

    Enter your guess: 100
    You won!
   ```

   ```
    SETUP PHASE

    Enter the magic number: 4
    Enter the maximum number of guesses: 2

    GAME PHASE

    Enter your guess: 1
    Too low! Try again.
    You have 1 guesses left.

    Enter your guess: 1
    You ran out of guesses. Too bad!
   ```

---

**Extra Assignment**

5. Write a Python script to accept a number `n` and create the following pattern:

    ```
    Enter n: 4
   🥔️🥔️🥔️🥔️🥔️🥔️🥔️🥔️🥔️🥔️🥔️
   🥔️️🦝🦝🦝🦝🥔️️🐶🐶🐶🐶🥔️️
   🥔️️🦝🦝🦝🦝🥔️️🐶🐶🐶🐶🥔️️
   🥔️️🦝🦝🦝🦝🥔️️🐶🐶🐶🐶🥔️️
   🥔️️🦝🦝🦝🦝🥔️️🐶🐶🐶🐶🥔️️
   🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️
   🥔️️🐘🐘🐘🐘🥔️️🐆🐆🐆🐆🥔️️
   🥔️️🐘🐘🐘🐘🥔️️🐆🐆🐆🐆🥔️️
   🥔️️🐘🐘🐘🐘🥔️️🐆🐆🐆🐆🥔️️
   🥔️️🐘🐘🐘🐘🥔️️🐆🐆🐆🐆🥔️️
   🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️🥔️️
    ```
