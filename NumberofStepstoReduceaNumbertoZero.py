
def numberOfSteps(num: int) -> int:
    ret = 0
    while(num > 0):
        num = num - 1 if num%2!=0 else num/2
        ret+=1
    return ret

if __name__ == '__main__':
    print(numberOfSteps(14))