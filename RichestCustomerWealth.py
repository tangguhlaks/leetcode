import sys
from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
   return max([sum(account) for  account in accounts])

if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(maximumWealth(accounts))
