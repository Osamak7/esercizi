def move_zeroes(nums:list[int]):
    lista_eliminati:list=[]
    for i in range(len(nums)):
        if nums[i] == 0:
            x=nums.pop(i)
            nums.append(x)
    return nums
print(move_zeroes([0,1,0,3,12]))