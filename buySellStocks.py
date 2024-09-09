def maxProfit(prices) -> int:
        result = 0
        left = 0
        right = 1
        while left<right and right<len(prices):
            #if you find a smaller digit shift to it
            if prices[left]>prices[right]:
                left = right
                right+=1
                continue
            #otherwise calc the profit and compare it with max_profit
            if prices[left]<prices[right]:
                current = prices[right]-prices[left]
                if current>result:
                    result = current
                right+=1
            #if this is also false just increment right
            else:
            
                right+=1

        return result



print(maxProfit([7,1,5,3,6,4]))