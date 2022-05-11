
def show(n):
    assert n > 0, "Only Positive Number of Terms Allowed"
    if n == 1:
        return 0
    if n == 2:
        return 1

    summ = show(n-1)+show(n-2)
    print(summ, " ")
    return summ


def main():
    n = int(input())
    x = show(n)
    print(x, " ")


if __name__ == '__main__':
    main()
