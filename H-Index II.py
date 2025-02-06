class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations_len = len(citations)

        left, right = 0, citations_len - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= citations_len - mid:
                right = mid - 1
            else:
                left = mid + 1

        return citations_len - left

sol = Solution()
print(sol.hIndex(citations = [0,1,4,5,6]))



