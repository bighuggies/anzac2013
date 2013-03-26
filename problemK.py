import sys

vowels = ['a', 'i', 'y', 'e', 'o', 'u']
consonants = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
vowelsUpper = [c.upper() for c in vowels]
consonantsUpper = [c.upper() for c in consonants]

vowLen = len(vowels)
conLen = len(consonants)

def main():
    for l in sys.stdin:
        l = list(l.strip())

        for i,c in enumerate(l):
            if c.istitle():
                if c in vowelsUpper:                
                    pos = vowelsUpper.index(c)
                    l[i] = vowelsUpper[(pos+vowLen/2) % vowLen]
                elif c in consonantsUpper:
                    pos = consonantsUpper.index(c)
                    l[i] = consonantsUpper[(pos+conLen/2) % conLen]
            else:
                if c in vowels:                
                    pos = vowels.index(c)
                    l[i] = vowels[(pos+vowLen/2) % vowLen]
                elif c in consonants:
                    pos = consonants.index(c)
                    l[i] = consonants[(pos+conLen/2) % conLen]
        print "".join(l)




if __name__ == '__main__':
    main()
