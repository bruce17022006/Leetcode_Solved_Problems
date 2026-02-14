class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        current = sum(cardPoints[:k]) 
        max_sum = current               
        for i in range(1, k + 1):
            current = current - cardPoints[k - i] + cardPoints[-i]
            max_sum = max(max_sum, current)

        return max_sum
