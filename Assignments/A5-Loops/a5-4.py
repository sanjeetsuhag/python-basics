print('SETUP PHASE\n')
magic_number = int(input('Enter the magic number: '))
max_guesses = int(input('Enter the maximum number of guesses: '))

print('\nGAME PHASE\n')
guess = int(input('Enter your guess: '))
guess_count = 1
while guess != magic_number and guess_count < max_guesses :
    if guess < magic_number:
        print('Too low! Try again.')
    else:
        print('Too high! Try again.')
    
    guesses_left = max_guesses - guess_count
    print(f'You have {guesses_left} guesses left.\n')
    guess = int(input('Enter your guess: '))
    guess_count = guess_count + 1

if guess_count == max_guesses:
    print('You ran out of guesses. Too bad!')

if guess == magic_number:
    print('You won!')