from mytools.resources.argparser import parse_args


def get_easter_date(year):
    j = int(year)

    a = j % 19
    b = j % 4
    c = j % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    x = 22 + d + e

    if x <= 31:
        m = 3

    else:
        m = 4
        x -= 31

    return x, m, j


def main():
    args, _ = parse_args()
    assert len(args) == 1, "Usage: python easter.py <year>"
    assert args[0].isdigit(), "Year must be a positive integer"

    day, month, year = get_easter_date(args[0])
    print(f"{day}.{month}.{year}")


if __name__ == "__main__":
    main()