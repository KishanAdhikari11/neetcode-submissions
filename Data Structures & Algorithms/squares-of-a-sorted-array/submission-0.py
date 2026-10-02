class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lp,rp=0,len(nums)-1
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        return sorted(nums)
        
        

        