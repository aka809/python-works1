user_input = input("Enter a list of integers separated by commas: ")
def find_ranges(nums):
    if not nums:
        return []
    ranges = []
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            if start == end:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{end}")
            start = nums[i]
    if start == nums[-1]:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}->{nums[-1]}")
    return ranges
nums = list(map(int, user_input.split(',')))
nums.sort()
result = find_ranges(nums)
print("Output:", result)