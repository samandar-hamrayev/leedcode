class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        diff_bit = xor_sum & - xor_sum
        num1, num2 = 0, 0
        for num in nums:
            if diff_bit & num:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
