def twoSum(nums: list[int], target: int) -> list[int]:
    for i, value in enumerate(nums):
        remainder = target - nums[i]
        nums[i] = None
        if remainder in nums:
            return [i, nums.index(remainder)]


twoSum([3, 2, 5, 3], 6)
