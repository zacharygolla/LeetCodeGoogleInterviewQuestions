def main():
    print(findSingleNumber([2, 3, 2, 3, 5, 6, 1, 6, 1, 5, 8]))


def findSingleNumber(nums=[]):
    # solution using set, time complexity O(n), space complexity(O(n))
    # dic = set()
    # for i in range(len(nums)):
    #     if nums[i] in dic:
    #         dic.remove(nums[i])
    #     else:
    #         dic.add(nums[i])

    # print(dic.pop())

    # solution using bitwise manipulation
    a = 0
    for i in nums:
        a ^= i
    return a


if __name__ == "__main__":
    main()
