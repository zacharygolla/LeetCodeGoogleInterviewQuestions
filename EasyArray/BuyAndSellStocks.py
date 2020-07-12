def main():
    print(maxProfit([7, 1, 5, 3, 6, 4]))


"""
"""


def maxProfit(trend=[]):
    if len(trend) == 0:
        return 0

    maxProfit = 0
    for i in range(1, len(trend)):
        if(trend[i] > trend[i-1]):
            maxProfit += trend[i] - trend[i-1]

    return maxProfit


if __name__ == "__main__":
    main()
