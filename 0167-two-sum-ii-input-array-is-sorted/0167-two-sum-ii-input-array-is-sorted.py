class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        for _ in range(len(numbers)):
            if(numbers[i]+numbers[j]==target):
                return([i+1,j+1])
                break
            if(numbers[i]+numbers[j]>target):
                j-=1
            if(numbers[i]+numbers[j]<target):
                i+=1
        else:
            return False