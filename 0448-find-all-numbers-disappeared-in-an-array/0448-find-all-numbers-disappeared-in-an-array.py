class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums_set=set(nums)
        def generate_list(start,end):
            return list(range(start,end+1))
        num=generate_list(1,n)
        missing=[]
        for number in num:
            if number not in nums_set:
                missing.append(number)
        return missing
        