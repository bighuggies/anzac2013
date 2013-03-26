def main():
    good = [1, 2, 3, 3, 4, 10]
    bad = [1, 2, 2, 2, 3, 5, 11]

    num_battles = int(raw_input())

    for i in xrange(num_battles):
        good_soldiers = [int(x) for x in raw_input().split(' ')]
        bad_soldiers = [int(x) for x in raw_input().split(' ')]

        good_scores = [z[0] * z[1] for z in zip(good, good_soldiers)]
        good_score = sum(good_scores)

        bad_scores = [z[0] * z[1] for z in zip(bad, bad_soldiers)]
        bad_score = sum(bad_scores)

        x = i + 1

        if good_score > bad_score:
            print("Battle {0}: Good triumphs over Evil".format(x))
        elif bad_score > good_score:
            print("Battle {0}: Evil eradicates all trace of Good".format(x))
        else:
            print("Battle {0}: No victor on this battle field".format(x))

if __name__ == '__main__':
    main()
