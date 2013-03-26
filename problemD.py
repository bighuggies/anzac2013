import sys


def solve(yThenX, start, end):
    


def main():
    while(True):
        size = int(sys.stdin.readline())

        if size == 0:
            break

        yThenX = []

        for x in xrange(size):
            yThenX.append([int(x) for x in sys.stdin.readline().split()])


        start = (0, 0)
        end = (size - 1, size - 1)

        solve(yThenX, start, end)

if __name__ == '__main__':
    main()
