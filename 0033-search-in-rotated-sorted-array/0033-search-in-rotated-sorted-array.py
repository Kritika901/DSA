class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        l, r = 0, n - 1
        while l < r:
            mid = (l + r + 1) // 2  
            if nums[mid] >= nums[0]:
                l = mid
            else:
                r = mid - 1
        pivot = l

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        if nums[0] <= target <= nums[pivot]:
            return binary_search(0, pivot)
        else:
            return binary_search(pivot + 1, n - 1)