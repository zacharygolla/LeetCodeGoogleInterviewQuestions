def main():
    rotateString(['h', 'e', 'l', 'l', 'o'])


def rotateString(charArray):
    start = 0
    end = len(charArray) - 1
    while((end - start) > 0):
        charArray[start], charArray[end] = charArray[end], charArray[start]
        start += 1
        end -= 1
    print(charArray)


if __name__ == "__main__":
    main()
