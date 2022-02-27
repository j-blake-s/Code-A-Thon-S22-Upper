
n, g = map(int, input().split())
nums = list(map(int, input().split()))
gifts = list(map(int, input().split()))
total = 0
pos = 0
seen = []
while pos < len(gifts):
    for person in nums:
        if gifts[pos] == person:
            found = False
            for s in seen:
                if s == person:
                    found = True
                    break
            if not found:
                seen.append(person)                
            total += 1
            nums.remove(person)
            break
    pos += 1
print(total, len(seen))