class Solution:
    def runningSum(self, nums):
        lastElement = 0
        sum=[]
        for i in range(len(nums)):      #[3,1,2,10,1]
            element = nums[i] + lastElement
            sum.append(element)
            lastElement = element
        return sum

ob = Solution()
sumArr = ob.runningSum([3,1,2,10,1])
print(sumArr)