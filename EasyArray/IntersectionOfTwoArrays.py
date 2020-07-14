# does not work
def main():
    intersection([3, 1, 2], [1, 1])


def intersection(nums1=[], nums2=[]):
    hashMap = {}
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    for num in nums1:
        count = 0
        if num in hashMap:
            hashMap.update(num=hashMap.get(num)+1)
        else:
            hashMap.update({num: count})

    k = 0
    for num in nums2:
        if num in hashMap and hashMap.get(num) > 0:
            nums1[k] = num
            k += 1
            hashMap.update(num=hashMap.get(num)-1)

    return nums1[k:]


if __name__ == "__main__":
    main()
