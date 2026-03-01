class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        m=0
        while right<len(prices):
            if(prices[right]>prices[left]):
                profit=prices[right]-prices[left]
                if(m<profit):
                    m=profit
            else:
                left=right
            right+=1
        return m

        