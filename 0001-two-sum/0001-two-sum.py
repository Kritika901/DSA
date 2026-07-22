class Solution:
    def twoSum(self, nums, target):
        n=len(nums) 
        dict={}
        for i in range(n) :
            rem= target-nums[i]
            if rem in dict:
                return [dict[rem],i]
            dict[nums[i]]=i  