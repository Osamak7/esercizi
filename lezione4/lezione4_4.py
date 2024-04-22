def majority_element(nums:list[int])->int:
    for n in nums:
        if nums.count(n)>len(nums)/2:
            return f"Il numero che si ripresenta più volte è : {n} "
    return None

print(majority_element([2,2,1,1,1,1,1,1,2,1,2]))