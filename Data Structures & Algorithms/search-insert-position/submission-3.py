class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]== target:
                return i
            elif i==0 and nums[i] > target:
                return 0
            elif i!=0:
                if nums[i]>target and nums[i-1]<target:
                    return i
                
                
        return i+1


            
        