import sys
from .binodfile import binodfunc


def main():
    args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))

    binodfunc(args[0])

if __name__ == '__main__':
    main()