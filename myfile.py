myList = [1]

def removeElement(nums,val):

        # left,right = 0,len(nums)-1
        # while left<right:


        #     if nums[right]==val:

        #         right-=1
        #     if nums[left]==val:
                
        #         nums[left] = nums[right]
        #         nums[right] = val


        #         right-=1
        #         left+=1
                
        #     else:
        #         left+=1
        # print(nums)
        # return right+1
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                  nums[k] = nums[i]
                  k+=1
        print(nums)
        return k
                  
print(removeElement(myList,1))