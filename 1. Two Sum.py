from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_ = {target-x: i for i, x in enumerate(nums)}
    for i, val in enumerate(nums):
        if hash_.get(val) is not None:
            if hash_[val] != i:
                return [i, hash_[val]]




nums = [-3,4,3,90]
target = 0
print(twoSum(nums, target))

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

nums = [0,4,3,0]
target = 0
print(twoSum(nums, target))

