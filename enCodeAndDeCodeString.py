from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append('#')
            parts.append(s)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i, n = 0, len(s)
        while i < n:
            j = i
            while j < n and s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res

strs = list(input("Nhập các từ cách nhau khoảng trắng: ").split())
s = Solution()
res = s.encode(strs)
print(s.encode(strs))
print(s.decode(res))