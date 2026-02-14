class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        op = []
        for i in nums:
            op.append(i)
        for i in nums:
            op.append(i)
        return op