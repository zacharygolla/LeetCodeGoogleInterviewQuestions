def main():
    containsDuplicates([1, 2, 3, 4])


def containsDuplicates(nums=[]):
    """
    #Set solution, Time Complexity O(n), Space complexity O(n)
    duplicates = False
    newSet = {}
    for i in range(len(nums)):
        if newSet.__contains__(nums[i]):
            duplicates = True
        newSet.update({nums[i]: 1})

    print(duplicates)
    """

    # Sort then check solution, Time complexity o(nlogn) because of sort, space complexity O(1)
    duplicates = False
    nums.sort()
    for i in range(1, len(nums)):
        if(nums[i] == nums[i-1]):
            duplicates = True

    print(duplicates)


if __name__ == "__main__":
    main()
