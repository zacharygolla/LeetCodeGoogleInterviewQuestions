def main():
    print(plusOne([9, 9, 9]))


def plusOne(nums=[]):
    counter = len(nums) - 1

    while counter >= 0:
        if nums[counter] == 9:
            if counter == 0:
                nums[counter] = 0
                return [1] + nums
            nums[counter] = 0
            counter -= 1
        else:
            nums[counter] += 1
            return nums


if __name__ == "__main__":
    main()
