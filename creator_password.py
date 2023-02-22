import string
import argparse
from random import choices


def create_password(length=8, upper=False, lower=False, digit=False,
                    pun=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if pool == '':
        pool += string.ascii_letters
    password = choices(pool, k=length)
    return ''.join(password)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a password creator')
    parser.add_argument(
        "length", type=int, help='Length of password'
    )
    parser.add_argument(
        "-u", '--upper', action='store_true', help='Upper char for password'
    )
    parser.add_argument(
        "-l", '--lower', action='store_true', help='Lower char for password'
    )
    parser.add_argument(
        "-d", '--digit', action='store_true', help='Numbers for password'
    )
    parser.add_argument(
        "-p", '--punctuation', action='store_true',
        help='Punctuation of ''password'
    )

    args = parser.parse_args()
    print(args)
    print(create_password(args.length, args.upper, args.lower, args.punctuation
                          , args.digit))

    # Go to terminal and type: python3 creator_password.py 20 -u -l -d -p
