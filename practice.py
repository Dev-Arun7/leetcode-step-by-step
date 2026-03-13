def my_function(nums):
    left = 0
    right = len(nums) -1
    max_area = 0

    while left < right:
        width = right - left
        current_height = min(nums[left],  nums[right])
        area = width * current_height

        max_area = max(area, max_area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return max_area




nums = [1,8,6,2,5,4,8,3,7]
result = my_function(nums)
print(result)

