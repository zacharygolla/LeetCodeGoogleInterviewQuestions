def main():
    print(twoSum([1, 6, 14, 25], 7))


def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return [dic[nums[i]], i]
        complement = target - nums[i]
        dic.update({complement: i})
    return []


if __name__ == "__main__":
    main()
