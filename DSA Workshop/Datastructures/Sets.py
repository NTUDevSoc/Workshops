a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Union (a | b): {a | b}")
print(f"Intersection (a & b): {a & b}")
print(f"Difference (a - b): {a - b}")
print(f"Symmetric Difference (a ^ b): {a ^ b}")

nums = [1, 2, 3, 4, 4, 5, 6, 2, 7, 2]

seen = set()
duplicates = set() # Use a set so you don't store '2' multiple times

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(f"Original list: {nums}")
print(f"Duplicates: {duplicates}") 
# Output: Duplicates: {2, 4}