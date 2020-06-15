def choose_func(nums, square_nums, remove_negatives):
    s = 0

    for num in nums:
        if num < 0:
            s += 1

    if s > 0:
        return remove_negatives(nums)
    return square_nums(nums)


def square_nums(nums):
        return [num ** 2 for num in nums]


def remove_negatives(nums):
        return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))