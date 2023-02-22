import random

print('wellcome to guess number')
top_range_number = input('Type a number: ')
if top_range_number.isdigit():
    top_range_number = int(top_range_number)

    if top_range_number <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time')
    quit()
random_number = random.randint(0, top_range_number)
score = 0
while True:
    score += 1
    user_guess = input('Type your guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue
    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print( 'type a lower number')
    else:
        print('type a larger number')

print(f'You got it in {score} guess')
