from typing import List


def runningSum(nums: List[int]) -> List[int]:
    ret = []
    for i in range(len(nums)):
        ret.append(sum(nums[:i + 1]))
    return ret

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(runningSum(nums))