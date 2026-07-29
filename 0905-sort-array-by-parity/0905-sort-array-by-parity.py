class Solution(object):
    def sortArrayByParity(self, nums):
        start=0
        n=len(nums)
        for i in range (0,n):
            if (nums[i]%2==0):
                temp=nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1
        return nums       