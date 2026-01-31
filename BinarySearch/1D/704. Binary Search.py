from math import floor
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st,end = 0,len(nums)-1

        while st<=end:
            mid = floor((st+end)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end = mid-1
            else:
                st = mid+1
        return -1
        
