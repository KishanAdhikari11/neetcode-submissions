class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zero_counter=0
        result=[]
        for num in nums: 
            if num ==0:
                zero_counter+=1
                continue
            else:
                product=product*num

        for num in nums:
            if zero_counter>1:
                return [0]*len(nums)
            elif zero_counter==1:
                if num==0:
                    result.append(product)
                else:
                    result.append(0)
            elif zero_counter==0:
                result.append(product//num)
        return result

        

        