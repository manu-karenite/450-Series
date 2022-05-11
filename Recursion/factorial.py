from time import time


def getAns(n):
    assert n >= 0, "Only Positive Allowed"
    if n in [0, 1]:
        return 1
    return n*getAns(n-1)


def main():
    st = time()
    n = int(input())
    print(getAns(n))
    et = time()

    print((et-st)*10**3)


if __name__ == "__main__":
    main()
