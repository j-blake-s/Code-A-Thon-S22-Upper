from collections import Counter
n, g = map(int, input().split())
nums = list(map(int, input().split()))
gifts = Counter(map(int, input().split()))
total = 0
seen = set()
# print(nums)
# print(gifts)
for x in nums:
    if gifts[x] > 0:
        if x not in seen:
            seen.add(x)
        gifts[x] -= 1
        total += 1
print(total, len(seen))