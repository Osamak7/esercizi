def intersection(nums1:list[int],nums2:list[int]):
    list3:list=[]
    for n in range(len(nums1)):
        if nums1[n]in nums2:
            list3.append(nums1[n])
    
    return list3
print(intersection([1,2,3,4,5,6,7,8,9],[2,3,4,5,1,6,44,55,66]))