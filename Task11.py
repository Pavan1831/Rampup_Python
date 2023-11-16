def beauty_of_subarray(arr, x):
    negatives = sorted([num for num in arr if num < 0])
    if len(negatives) < x:
        return 0
    return negatives[x - 1]

def beauty_of_subarrays(nums, k, x):
    result = []
    for i in range(len(nums) - k + 1):
        subarray = nums[i:i+k]
        beauty = beauty_of_subarray(subarray, x)
        result.append(beauty)
    return result

# Example
nums = [1, -1, -3, -2, 3]
k = 3
x = 2
output = beauty_of_subarrays(nums, k, x)
print(output)  # Output: [-1, -2, -2]
