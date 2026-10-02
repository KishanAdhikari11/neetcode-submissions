class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lp,rp=0,len(nums)-1
        res=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[rp])>abs(nums[lp]):
                res[i]=nums[rp]*nums[rp]
                rp-=1
            else:
                res[i]=nums[lp]*nums[lp]
                lp+=1
        return res
            
            
        
        

        