from collections import Counter


def ransomNote(ransomNote: str,magazine: str) -> bool:
    a = Counter(ransomNote)
    b = Counter(magazine)
    for char,count in a.items():
        if b[char] < count:
            return False
    return True

if __name__ == '__main__':
    print(ransomNote("aab","baa"))