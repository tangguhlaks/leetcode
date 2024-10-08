from typing import List


def dupZeros(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 0 and i!= len(nums)-1:
            for j in range(len(nums)-1,i,-1):
                nums[j] = nums[j-1]
            nums[i+1] = 0
            i+=1
        i+=1
    return nums

if __name__ == '__main__':
    print(dupZeros([0,4,1,0,0,8,0,0,3]))
