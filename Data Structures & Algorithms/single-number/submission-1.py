class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter={}
        for num in nums:
            if num in counter:
                counter[num] +=1
            else:
                counter[num]=1
        print(counter)
        for k,v in counter.items():
            if v ==1:
                return k
        