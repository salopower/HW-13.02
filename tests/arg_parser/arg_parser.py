import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", help="Enter your name")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
parser.add_argument("-H", "--helpmsg", help="Show help message and exit", action="store_true")

args = parser.parse_args()

if args.name:
    if args.name == "Valentin":
        print('Валєнтін, японскій бог, ти зачєм у ката яйца-та аткрутіл?!')
    else:
        print('Welcome, ' + args.name + '!')
else:
    print('Тут могла бути ваша... допомога =)')

