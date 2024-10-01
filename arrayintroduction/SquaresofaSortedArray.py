from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([x**2 for x in nums])

if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))