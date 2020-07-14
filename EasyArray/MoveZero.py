def main():
    print(moveZeros([0, 1, 0, 3, 12]))


def moveZeros(nums=[]):
    counter = 0
    for i in range(len(nums)):
        if (counter + i) > len(nums):
            nums[i-counter] = nums[i]
            nums[i] = 0
        else:
            nums[i-counter] = nums[i]
            if(nums[i] == 0):
                counter += 1
            if(i + counter) >= len(nums):
                nums[i] = 0

    return nums


if __name__ == "__main__":
    main()
