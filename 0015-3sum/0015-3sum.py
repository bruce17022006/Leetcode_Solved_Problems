class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        curr_sum=0
        nums_dict={val:idx for idx,val in enumerate(nums)}
        used=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                curr_sum=nums[i]+nums[j]
                target=-1*curr_sum
                if target in nums_dict:
                    k=nums_dict[target]
                    if k > j:
                         triplet = (nums[i], nums[j], target)
                         if triplet not in used:
                            result.append(list(triplet))
                            used.add(triplet)
        return result


        