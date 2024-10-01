from typing import List


def findNumber(nums: List[int]) -> int:
    ret = 0
    for i in nums:
        ret = ret+1 if len(str(i))%2==0 else ret+0
    return ret