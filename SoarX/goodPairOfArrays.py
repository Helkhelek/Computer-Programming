class Solution(object):
    def numIdenticalPairs(self, nums):
        i=0
        j=1
        pair = 0
        while j < len(nums): #j start 1 so that we don't get indexing error as the last element doesn't need a check
            k = i+1
            while k<len(nums):
                if nums[i]==nums[k]: # and i<k if i+1 was not there
                    pair+=1
                    print(i, k)
                k+=1
            i+=1
            j+=1
        return pair

ob = Solution()
numberOfPairs = ob.numIdenticalPairs([1,2,3])
print("Number of Pair : ", numberOfPairs)

        