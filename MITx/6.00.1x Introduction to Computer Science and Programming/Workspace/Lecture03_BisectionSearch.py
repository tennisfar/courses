low = 0
high = 100
ans = ''
guess = ''

print('Please think of a number between 0 and 100!')

while ans != 'c':
    guess = (high + low) / 2

    while True:
        print('Is your secret number ' + str(guess) + '?')
        ans = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')

        if (ans == 'h') or (ans == 'l') or (ans == 'c'):
            break
        else:
            print('Sorry, I did not understand your input.')

    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess

print('Game over. Your secret number was: ' + str(guess))
