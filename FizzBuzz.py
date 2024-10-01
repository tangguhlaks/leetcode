from typing import List


def fizzbuzz(n:int) -> List[str]:
    ret = ["FizzBuzz" if x%3==0 and x%5==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else str(x) for x in range(1,n+1)]
    return ret

if __name__ == '__main__':
    n = 5
    print(fizzbuzz(n))