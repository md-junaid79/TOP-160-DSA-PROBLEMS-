def maximumProfit(self, prices) -> int:
    
        #accumulate the profit by checking if the next price is greater than the current price
        #if it is, we add the difference to the profit
        
        res=0   
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                res+=prices[i+1]-prices[i]
                
        return res