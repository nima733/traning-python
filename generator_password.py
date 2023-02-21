import string
import random
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')


def generate_password():
    password_length = int(input('How long would you like password to be? '))
    password = list()
    for x in range(password_length):
        password.append(random.choice(characters))
    password = ''.join(password)
    print(password)


option = input('Do you want to generate a password? (yes/no)')
option.lower()
if option == 'yes':
    generate_password()
elif option == 'No':
    print('Program ended')
    quit()
else:
    print('Invalid input, please input yes or no')
