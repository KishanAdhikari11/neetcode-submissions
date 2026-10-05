class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = 0

        temp = []

        while left < len(nums1) and right < len(nums2):

            if nums1[left] < nums2[right]:
                temp.append(nums1[left])
                left += 1
            else:
                temp.append(nums2[right])
                right += 1

        while left < len(nums1):
            temp.append(nums1[left])
            left += 1

        while right < len(nums2):
            temp.append(nums2[right])
            right += 1
        print(temp)
        if len(temp)%2==0:
            return (temp[len(temp)//2]+temp[len(temp)//2-1])/2
        else:
            return temp[len(temp)//2]