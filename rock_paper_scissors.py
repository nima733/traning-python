import random

user_wins = 0
pc_win = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/scissors or Q to quit: ').lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper:1, scissors:2
    pc_pick = options[random_number]
    print(f'Computer picked {pc_pick}.')
    if user_input == 'rock' and pc_pick == 'scissors':
        print('you win!')
        user_wins += 1
        continue
    if user_input == 'paper' and pc_pick == 'rock':
        print('you win!')
        user_wins += 1
        continue
    if user_input == 'scissors' and pc_pick == 'paper':
        print('you win!')
        user_wins += 1
        continue
    else:
        print('computer is win')
        pc_win += 1

print(f'You win {user_wins} times')
print(f'computer win {pc_win} times ')
print('good bye')
