# Anagram = hai chuỗi có cùng số lượng và loại ký tự, nhưng thứ tự có thể khác
class Solution:
    # Cách 1: dùng cho kí tự bất kì
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS = 1 + countS.get(s[i], 0)
            countT = 1 + countT.get(t[i], 0)
        return countS == countT
    
    # Cách 2: chỉ dùng cho kí tự thường
    def isAnagram2(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True

s = Solution()
s1 = input("Nhập chuỗi kí tự s, mỗi kí tự cách nhau 1 khoảng trắng: ").split()
s2 = input("Nhập chuỗi kí tự t, mỗi kí tự cách nhau 1 khoảng trắng: ").split()
print(s.isAnagram(s1,s2))
print(s.isAnagram2(s1,s2))



