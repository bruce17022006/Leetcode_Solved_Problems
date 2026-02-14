class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=nums1 + nums2
        arr=sorted(merge)
        if(len(arr)%2==1):
            return float(arr[len(arr)//2])
        else:
            mid=len(arr)//2
            return (arr[mid-1]+arr[mid]) / 2.0