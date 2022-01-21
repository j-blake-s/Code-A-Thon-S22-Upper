import string
def gen(so_far='', in_state1=True):
    global total

    if not in_state1 and len(so_far) >= n / 2:
        total += 1
        return
    if len(so_far) == (n - gap) // 2:
        in_state1 = False
    if in_state1:
        possible = odd_letters - ({so_far[-1]} if len(so_far) else set())
    else:
        possible = even_letters - ({so_far[-1]} if len(so_far) else set())

    for letter in possible:
        gen(so_far + letter, in_state1)

cases = int(input())
for _ in range(cases):
    n, gap, num_letters_allowed = map(int, input().split())
    allowed_letters = set(string.ascii_uppercase[:num_letters_allowed])
    odd_letters = {x for x in allowed_letters if ord(x) % 2 == 1}
    even_letters = {x for x in allowed_letters if ord(x) % 2 == 0}
    assert even_letters == allowed_letters - odd_letters
    total = 0
            

    if n % 2 != gap % 2 or gap % 2 == 0:
        print(0)
    else:
        gen()
        print(total)


