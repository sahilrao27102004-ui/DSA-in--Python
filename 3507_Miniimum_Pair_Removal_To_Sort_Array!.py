class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        while nums!=sorted(nums):
            index=0
            
            for i in range(len(nums)-1): #len(nums)-1 because we checking pairs so we can do it without last element.
                if nums[index]+nums[index+1]>nums[i]+nums[i+1]:
                    index=i
            minimum=nums[index]+nums[index+1]
            nums[index]=minimum
            nums.pop(index+1)

            count+=1

        return count