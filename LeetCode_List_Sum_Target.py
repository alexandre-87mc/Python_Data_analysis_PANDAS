nums = [1,2,3,4,5]
t=9
prevMap = {} #val : index

for i, n in enumerate(nums):
    diff = t - n
    if diff in prevMap:
        print([prevMap[diff],i])
    prevMap[n]=i
