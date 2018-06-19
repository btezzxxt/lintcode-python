def bs_min_i_eq_key(nums, key):
    l = 0
    r = len(nums)-1
    while l<r:
        m=l+(r-l)//2
        if nums[m] < key:
            l = m+1
        else:
            r = m
    if nums[r]==key:
        return r
    return -1

def bs_max_i_eq_key(nums, key):
    l = 0
    r = len(nums)-1
    while l < r:
        m = l + (r-l+1)//2
        if nums[m] > key:
            r = m - 1
        else:
            l = m
    if nums[l] == key:
        return l
    return -1

def bs_min_i_gt_key(nums, key):
    l = 0 
    r = len(nums)-1
    while l<r:
        m = l + (r-l)//2
        if nums[m] <= key:
            l = m+1
        else:
            r = m
    if nums[r] > key:
        return r
    return -1

def bs_max_i_lt_key(nums, key):
    l = 0
    r = len(nums) -1
    while l<r:
        m = l + (r-l+1)//2
        if nums[m] >= key:
            r = m -1
        else:
            l = m
    if nums[l] < key:
        return l
    return -1

print(bs_min_i_eq_key([1,1,2,3,3,3,3,4,5,5], 5), "\n")
print(bs_max_i_eq_key([1,1,2,3,3,3,3,4,5,5], 5), "\n")
print(bs_min_i_gt_key([1,1,2,3,3,3,3,4,5,5], 2), "\n")
print(bs_max_i_lt_key([1,1,2,3,3,3,3,4,5,5], 0), "\n")



