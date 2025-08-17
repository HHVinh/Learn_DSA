from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])   # độ dài chuỗi
            i = j + 1              # nhảy qua dấu #
            j = i + length         # vị trí kết thúc
            res.append(s[i:j])     # lấy chuỗi
            i = j                  # cập nhật i
        return res

strs = list(input("Nhập các từ cách nhau khoảng trắng: ").split())
s = Solution()
res = s.encode(strs)
print(s.encode(strs))
print(s.decode(res))

