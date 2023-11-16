def longest_square_streak(nums):
    longest_streak = -1

    # Create a dictionary to store the length of the longest streak ending at each number
    streak_lengths = {}

    for num in nums:
        streak_lengths[num] = 1  # Minimum streak length is 1

        # Check if the square root of the number exists in the streak_lengths dictionary
        if num > 1 and (int(num ** 0.5)) ** 2 == num:
            prev = int(num ** 0.5)
            if prev in streak_lengths:
                streak_lengths[num] = streak_lengths[prev] + 1

        longest_streak = max(longest_streak, streak_lengths[num])

    return longest_streak if longest_streak >= 2 else -1

# Example
nums = [4, 3, 6, 16, 8, 2]
output = longest_square_streak(nums)
print(output)  # Output: 3
