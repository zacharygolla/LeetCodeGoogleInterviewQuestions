def main():
    print(validAnagram('anagram', 'nagamar'))


def validAnagram(s, t):
    # first method using sort, python uses tim sort. best cost o(n) worst case o(nlogn)
    # anagram = False
    # # make sure they are same length
    # if len(s) != len(t):
    #     return anagram
    # # python uses timsort. o(n) best case
    # s = sorted(s)
    # t = sorted(t)

    # if(s == t):
    #     anagram = True

    # return anagram

    # second method use stagnant size list
    if(len(s) != len(t)):
        return False

    counter = {}
    for i in range(len(s)):
        if s[i] in counter:
            counter.update({s[i]: counter.get(s[i]) + 1})
        else:
            counter.update({s[i]: 1})

        if t[i] in counter:
            counter.update({t[i]: counter.get(t[i]) - 1})
        else:
            counter.update({t[i]: -1})

    for count in counter:
        if counter.get(count) != 0:
            return False

    return True


if __name__ == "__main__":
    main()
