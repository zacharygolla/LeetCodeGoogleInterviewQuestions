def main():
    print(firstUniqueCharacter("dddccdbba"))


def firstUniqueCharacter(s):
    count = {}
    for i in range(len(s)):
        c = s[i]
        if count.get(c) is None:
            count.update({c: 1})
        else:
            count.update({c: count.get(c) + 1})

    for i in range(len(s)):
        if count.get(s[i]) == 1:
            return i

    return -1


if __name__ == "__main__":
    main()
