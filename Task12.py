def sum_of_powers(nums):
    MOD = 10**9 + 7
    result = 0
    for i in range(len(nums)):
        max_val = nums[i]
        min_val = nums[i]
        for j in range(i, len(nums)):
            max_val = max(max_val, nums[j])
            min_val = min(min_val, nums[j])
            power = (max_val * max_val) * (min_val * min_val)
            result = (result + power) % MOD
    return result

# Example
nums = [2, 1, 4]
output = sum_of_powers(nums)
print(output)
