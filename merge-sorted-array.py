def merge(nums1: list[int], n1: int, nums2: list[int], n2: int) -> list[int]:
    i1 = n1 - 1
    i2 = n2 - 1
    index = n1 + n2 - 1
    while i2 >= 0:
        if i1 >= 0 and nums1[i1] >= nums2[i2]:
            nums1[index] = nums1[i1]
            i1 -= 1
        else:
            nums1[index] = nums2[i2]
            i2 -= 1
        index -= 1
    return nums1

result = merge(nums1 = [1,2,3,0,0,0], n1 = 3, nums2 = [2,5,6], n2 = 3)
print(result)
