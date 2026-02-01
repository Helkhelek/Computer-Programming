class Solution:
    def getConcatenation(self, nums):
        ans = nums
        ans.extend(nums)
        return ans

ob = Solution()
arr = ob.getConcatenation([1,3,2,1])
print(arr)