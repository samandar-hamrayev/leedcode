def findDifference(nums1: list[int], nums2: list[int])-> list[list[int]]:
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


print(findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))