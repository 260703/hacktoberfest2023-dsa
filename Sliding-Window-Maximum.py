# this is leet code solution (239)

from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []

    result = []
    window = deque()

    for i in range(len(nums)):
        # Remove elements that are out of the current window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements that are smaller than the current element
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        # Add the maximum element of the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Example usage:
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = maxSlidingWindow(nums, k)
print(result)  # Output: [3,3,5,5,6,7]
