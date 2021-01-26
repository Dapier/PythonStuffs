secret_number = 9
guess_cout = 0
guess_limit = 3
while guess_cout < guess_limit:
    guess = int(input('Guess: '))
    guess_cout +=1
    if guess == secret_number:
        print('You won')
        break
else:
    print("Sorry, you failed")