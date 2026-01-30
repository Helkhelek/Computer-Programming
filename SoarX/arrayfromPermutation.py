class Solution:
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

ob = Solution()
arr = ob.buildArray([5,0,1,2,3,4])
print(arr)
        