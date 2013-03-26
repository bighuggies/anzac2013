import sys


def main():
    numcases = int(sys.stdin.readline())

    for i in xrange(numcases):
        f = int(sys.stdin.readline())

        components = [set(sys.stdin.readline().split())]
        print(len(components[0]))

        for pair in xrange(f - 1):
            friends = sys.stdin.readline().split()
            numComponentsPairIsIn = 0
            eitherPersonInAComponent = False
            finalComponent = components[0]

            for s in components:
                for person in friends:
                    if person in s:
                        eitherPersonInAComponent = True
                        numComponentsPairIsIn += 1

                        if numComponentsPairIsIn > 1:
                            s.update(s.union(finalComponent))
                            del components[components.index(finalComponent)]
                            numComponentsPairIsIn = 1

                        s.update(friends)
                        finalComponent = s

                        break

            if eitherPersonInAComponent is False:
                newComponent = set(friends)
                components.append(newComponent)
                finalComponent = newComponent

            print(len(finalComponent))


if __name__ == '__main__':
    main()