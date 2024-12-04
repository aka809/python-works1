def find_closest_num(nums):
    if not nums:
        return None
    nums.sort(key=lambda x:(abs(x),-x))
    return nums[0]
nums=[-4,-2,1,3-1]
result=find_closest_num(nums)
print(result)