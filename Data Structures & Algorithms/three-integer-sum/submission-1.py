class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp=set()
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left < right:
                vals=nums[i]+nums[left]+nums[right]
                if vals==0:
                    temp.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif vals> 0:
                    right-=1
                else:
                    left+=1
        res=[list(x) for x in temp]
        return res


        
    


        