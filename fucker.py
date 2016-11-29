# This program corrupts files on purpose.
# I intend to use it for art.

import argparse
import random
from sys import stderr


def main():
    parser = argparse.ArgumentParser(description='f u c k e r')
    parser.add_argument('file', nargs=1, type=argparse.FileType('rb'))
    parser.add_argument('--generations', '-g', nargs=1, type=int, default=1)
    parser.add_argument('--seed', '-s', nargs=1, type=int, default=None)
    parser.add_argument('--write', '-w', type=boolean, default=False)
    parser.add_argument('--one', '-1', type=boolean, default=False)
    args = parser.parse_args()

    print("Seed is {}".format(args.seed), file=stderr)
    random.seed(args.seed)
    print("Reading file..", file=stderr)
    data = args.file[0].read()
    if not args.write:
        print(fuck(data, args, carry=args.generations), end="")
    else:
        fuck(data, args, carry=args.generations)


def fuck(data, args, carry=0):
    # Do fucking up.
    # Add something at a random spot along the way.
    s = random.randrange(0, len(data))
    garbage = bytearray([random.randint(0, 255)
                         for a in range(random.randint(1, 200))])
    data = data[:s] + garbage + data[s:]

    if args.write:
        with open("fucker-{}-{}".format(args.generations - carry, args.file[0].name), "w+") as f:
            f.write(data)
    if carry > 1:
        return fuck(data, args, carry - 1)
    else:
        return data

if __name__ == '__main__':
    main()
