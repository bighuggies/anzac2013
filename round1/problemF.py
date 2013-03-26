def main():
    numProbs = int(raw_input())

    for D in xrange(numProbs):
        raw_input()
        ASCII = raw_input().strip('\r\n')

        raw_input()
        xlist = [int(x) for x in raw_input().split(' ')] #all numbers between 2 and -2

        currentindex = 0
        output = []
        for x in xlist:
            currentindex += x
            currentindex = currentindex % len(ASCII)
            output.append(str(ASCII[currentindex]))

        print "{0} {1}".format(D+1, "".join(output))

if __name__ == '__main__':
    main()
