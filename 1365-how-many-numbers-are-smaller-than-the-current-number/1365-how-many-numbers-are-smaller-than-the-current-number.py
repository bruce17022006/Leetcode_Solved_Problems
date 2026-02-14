class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        buckets=[0]*102
        for num in nums:
            buckets[num]+=1
        for i in range(1, len(buckets)):
            buckets[i] += buckets[i - 1]
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(buckets[num - 1])
        return result    