class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        mp = {}
        for num in nums1:
            mp[num] = mp.get(num, 0) + 1

        result = []
        for num in nums2:
            if num in mp:
                result.append(num)
                mp[num] -= 1
                if mp[num] == 0:
                    del mp[num]
        return result


sol = Solution()
print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

