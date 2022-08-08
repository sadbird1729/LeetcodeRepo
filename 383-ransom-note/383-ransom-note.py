class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0]*26
        for x in magazine:
            record[ord(x)-ord('a')] += 1
        for x in ransomNote:
            record[ord(x)-ord('a')] -= 1
        for i in record:
            if i < 0:return False
        return True