class Solution(object):
    def peakIndexInMountainArray(self, nums):
        n=len(nums)
        l,r=0,n-2
        ans=n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans