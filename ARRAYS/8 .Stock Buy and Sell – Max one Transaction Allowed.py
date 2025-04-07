def maximumProfit(self, prices):

        res=0
        minsofar=prices[0]
        
        for i in range(1,len(prices)):
            #check if the current price is less than the minimum price so far
            minsofar=min(minsofar,prices[i])
            
            #maximize the profit by checking if the current price is greater than the minimum price so far
            res=max(res,prices[i]-minsofar)
            
        return res