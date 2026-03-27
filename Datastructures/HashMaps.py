
def two_sum(nums, target):
    seen_map = {}
    for i, num in enumerate(nums):

        complement = target - num

        if complement in seen_map:
            return [seen_map[complement], i]
        
        else:
            seen_map[num] = i

    return False

nums = [1,2,3,6,8,12,15,17]

target = 18

print(f"The indexes of {nums} that make {target} are:", two_sum(nums, target))
