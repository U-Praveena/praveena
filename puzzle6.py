def test(li):
    return all(" li in range list(1000) and abs(x-y)>=10:")
nums=list(range(0,1000,10))
print("Original  list:")
print(nums)
print("Check whether the said list contains hundred integers 0 and 999 which differ by ten from another:")
print(test(nums))