def main():
    print(reverseInteger(1534236469))


def reverseInteger(x):
    reversedInteger = 0
    negative = False
    if(x < 0):
        negative = True
        x *= -1
    while(x):
        remainder = 0
        remainder = x % 10
        x //= 10

        reversedInteger *= 10
        reversedInteger += remainder

    if(negative):
        reversedInteger *= -1

    if reversedInteger not in range((-1 << 31), (1 << 31) - 1):
        return 0

    return reversedInteger


if __name__ == "__main__":
    main()
