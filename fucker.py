#!/usr/bin/env python3
# This program corrupts files on purpose.
# I intend to use it for art.

import argparse
import random
from sys import stderr, setrecursionlimit
from os import path

setrecursionlimit(20000)

def main():
    parser = argparse.ArgumentParser(description='f u c k e r is a tool for the controlled destruction of files for fun and profit.')
    parser.add_argument('file', nargs=1, type=argparse.FileType('rb'), help="file to be fucked (required)")
    parser.add_argument('--generations', '-g', nargs=1, type=int, default=[1], help="number of generations to output")
    parser.add_argument('--fuck', '-f', action='count', default=0, help="fucking level (pass argument multiple times for greater effect!)")
    parser.add_argument('--seed', '-s', nargs=1, type=int, default=[0], help='set the random seed if needed')
    parser.add_argument('--write', '-w', action="store_true", help="write out files (default is stdout)")
    parser.add_argument('--path', '-p', nargs=1, type=str, default=['.'], help="write path when using writing files")
    parser.add_argument('--final', action="store_true", help="write only the final file")
    args = parser.parse_args()

    if args.seed[0] != 0:
        print('Setting seed: {}'.format(args.seed[0]), file=stderr)
        random.seed(args.seed[0])
    print('Reading file..', file=stderr)
    print('Fucking level is {}.'.format(args.fuck))
    data = args.file[0].read()
    if not args.write:
        print(fuck(data, args, carry=args.generations[0]), end='')
    else:
        fuck(data, args, carry=args.generations[0])


def fuck(data, args, carry=0):
    # Do fucking up.
    # Add something at a random spot along the way.
    s = random.randrange(0, len(data))
    garbage = bytearray([random.randint(0, 255)
                         for a in range(random.randint(1, args.fuck + 1))])
    data = data[:s] + garbage + data[s:]

    if args.write:
        if (args.final and carry == 1) or not args.final:
            fn = path.join(args.path[0], 'fucked-{:06d}-{}'.format(args.generations[0] - carry, path.basename(args.file[0].name)))
            with open(fn, 'wb+') as f:
                print('Writing to {}...'.format(fn))
                f.write(data)
    if carry > 1:
        return fuck(data, args, carry - 1)
    else:
        return data

if __name__ == '__main__':
    main()
