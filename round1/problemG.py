def main():
    numProbs = int(raw_input())

    for i in xrange(numProbs):
        l = raw_input()
        s = l.strip()
        l = int(l)

        answer = 0
        while l != 0:
            answer += sum(xrange(l + 1))
            l -= 1

        print "{0}: {1} {2}".format(i + 1, s, answer)

if __name__ == '__main__':
    main()
