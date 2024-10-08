from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Pointer for the last index in nums1 where the element should go.
    last = m + n - 1
    m -= 1
    n -= 1

    # Merge in reverse order.
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[last] = nums1[m]
            m -= 1
        else:
            nums1[last] = nums2[n]
            n -= 1
        last -= 1

    # Fill nums1 with remaining elements from nums2 if any.
    while n >= 0:
        nums1[last] = nums2[n]
        n -= 1
        last -= 1

    print(nums1)

if __name__ == '__main__':
    merge(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ,0,
    [-50, -50, -48, -47, -44, -44, -37, -35, -35, -32, -32, -31, -29, -29, -28, -26, -24, -23, -23, -21, -20, -19, -17, -15, -14, -12, -12, -11, -10, -9, -8, -5, -2, -2, 1, 1, 3, 4, 4, 7, 7, 7, 9, 10, 11, 12, 14, 16, 17, 18, 21, 21, 24, 31, 33, 34, 35, 36, 41, 41, 46, 48, 48]
    ,63)
