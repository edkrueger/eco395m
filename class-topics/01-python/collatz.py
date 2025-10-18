def collatz(z):

    s = z

    print(s)

    while s != 1:

        if s % 2 == 0:
            s = s // 2
        else:
            s = 3 * s + 1

        print(s)

collatz(51)