class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        indexed_nums = list(enumerate(numbers)) 
        indexed_nums.sort(key=lambda x: x[1])
        left=0
        n=len(indexed_nums)-1
        right=n
        while left < right:
            current_sum = indexed_nums[left][1] + indexed_nums[right][1]
            if current_sum == target:
                return [indexed_nums[left][0],indexed_nums[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1