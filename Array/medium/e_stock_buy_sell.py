def maxProfit(self, prices) -> int:
        buy=prices[0]
        profit=0
        for i in range(len(prices)):
            if buy > prices[i]:
                buy=prices[i]
            elif prices[i]-buy > profit:
                profit=prices[i]-buy
        return profit