from random import randint
import string
import argparse


def getargs():
     parser = argparse.ArgumentParser(
         prog='passgen.py',
         description='random password generator',
         epilog='\u00A9 Fedor Klochkov'
     )
     parser.add_argument('-b', '--big', action='store_true', help='include big letters into the password')

     parser.add_argument('-s', '--spec', action='store_true', help='include special simbols into the password')

     parser.add_argument('p_len', type=int, default=10, nargs='?', help='password length')

     parser.add_argument('p_count', type=int, default=1, nargs='?', help='password count')

     return parser.parse_args()


def passgen(len_=8, b=False, s=False):
    a = string.digits + string.ascii_lowercase
    password = ''
    if b:
        a += string.ascii_uppercase
    if s:
        a += string.punctuation
    for i in range(len_):
        password += a[randint(0, len(a)-1)]
    return password


if __name__ == '__main__':
    args = getargs()
    for i in range(args.p_count):
        print(passgen(len_=args.p_len, b=args.big, s=args.spec))
