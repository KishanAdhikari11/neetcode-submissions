class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsSet={}
        for num in nums:
            if num in numsSet:
                numsSet[num]+=1
            else:
                numsSet[num]=1
        sorted_nums=sorted(numsSet,key=numsSet.get,reverse=True)
        return sorted_nums[:k]
       
        
            