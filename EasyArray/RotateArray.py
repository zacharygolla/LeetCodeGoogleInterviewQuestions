"""
rotate an array k number of steps
Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,
"""


def main():
    rotateArray([-1, -100, 3, 99], 2)


def rotateArray(nums: [], k):
    k = k % len(nums)

    start = 0
    count = 0
    nextPosition = 1
    while count < len(nums):
        current, prev = start, nums[start]
        while start != nextPosition:
            nextPosition = (current + k) % len(nums)
            nums[nextPosition], prev = prev, nums[nextPosition]
            current = nextPosition
            count += 1
        start += 1

    print(nums)


if __name__ == "__main__":
    main()
