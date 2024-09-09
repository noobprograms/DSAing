def canJump( nums):
    # lastIndex = len(nums)-1
    # for i in range(len(nums)):
    #     if nums[i]>=lastIndex-i:
    #         return True
    #start from the end and keep shifting your goal 
    goal = len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i]>=goal:
            goal =i 

    return True if goal==0 else False