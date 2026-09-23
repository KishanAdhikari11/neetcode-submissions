class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        if len(nums) == 0:
            return 0
        longest=1
        for num in nums:
            count=1
            if num-1 not in numSet:
                while (num+1) in numSet:
                    count+=1
                    num+=1
                    longest=max(longest,count)
        return longest

        