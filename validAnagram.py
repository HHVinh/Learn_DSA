# Anagram = hai chuỗi có cùng số lượng và loại ký tự, nhưng thứ tự có thể khác
class Solution:
    # Cách 1: dùng cho kí tự bất kì
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
    # Cách 2: dùng 1 dict và cho bất kì kí tự
    def isAnagram2(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False    
        count = {}  # Dùng 1 dict để vừa tăng vừa giảm
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        # Nếu tất cả giá trị đều = 0 thì là anagram
        for val in count.values():
            if val != 0:
                return False
        return True

    # Cách 3: chỉ dùng cho kí tự thường
    def isAnagram3(self, s: str, t: str) -> bool:
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



