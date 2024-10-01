from typing import List


def maxOnes(nums: List[int]) -> int:
    ret = 0
    mx = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            ret += 1
        else:
            mx = max(ret,mx)
            ret = 0
    return max(mx,ret)

if __name__ == '__main__':
    print("-> ",maxOnes([1,1,0,1,1,1]))