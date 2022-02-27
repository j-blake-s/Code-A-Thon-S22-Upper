import string
from functools import *
@lru_cache(maxsize=None)
def gen(so_far=0, in_state1=True):
    before = in_state1
    if not in_state1 and (so_far) >= n / 2:
        return 1
    if (so_far) == (n - gap) // 2:
        in_state1 = False
    if in_state1:
        possible = len(odd_letters) - (1 if (so_far) else 0)
    else:
        possible = len(even_letters) - (0 if (before) else 1)
    # print(possible)
    return sum(gen(so_far + 1, in_state1) for _ in range(possible))

cases = int(input())
for _ in range(cases):
    gen.cache_clear()
    n, gap, num_letters_allowed = map(int, input().split())
    allowed_letters = set(string.ascii_uppercase[:num_letters_allowed])
    odd_letters = {x for x in allowed_letters if ord(x) % 2 == 1}
    even_letters = {x for x in allowed_letters if ord(x) % 2 == 0}
    assert even_letters == allowed_letters - odd_letters
    if n % 2 != gap % 2 or gap % 2 == 0:
        print(0)
    else:
        ret = (gen())
        # assert ret < 2 ** 31
        print(ret)

        
        




