def getDiscount(discountvalue):
    total  = 1000
    mainMap = {"CouponOne":100,"CouponTwo":200,"CouponThree":300}

    return total-mainMap[discountvalue]

print(getDiscount("CouponTwo"))

