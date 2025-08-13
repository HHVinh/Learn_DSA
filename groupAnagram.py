from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list): Tự tạo list rỗng nếu key chưa tồn tại
        res = defaultdict(list)
        
        for s in strs:
            # sorted(s) -> Trả về list ký tự đã sắp xếp theo thứ tự alphabet
            # ''.join(list) -> Ghép các ký tự thành chuỗi cách nhau kí tự không rỗng
            sortedS = ''.join(sorted(s))
            
            # Dùng chuỗi đã sắp xếp làm key, thêm từ gốc vào nhóm
            res[sortedS].append(s)
        
        # res.values() là các nhóm, chuyển sang list
        return list(res.values())


"""
Thuật toán:
1. Mỗi anagram khi sắp xếp lại ký tự sẽ cho cùng một chuỗi chuẩn.
2. Dùng chuỗi chuẩn đó làm key trong dict.
3. Gom các từ có cùng key vào một list.
4. Trả về tất cả list đó.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Tự tạo list rỗng nếu key chưa có
        
        for s in strs:
            # Mảng đếm số lần xuất hiện mỗi ký tự (26 chữ cái)
            count = [0] * 26
            
            for c in s:
                # ord(c) -> Lấy mã ASCII/Unicode của ký tự c
                # ord('a') = 97 → ord(c) - ord('a') sẽ cho số từ 0 đến 25
                count[ord(c) - ord('a')] += 1
            
            # tuple(list) -> chuyển list thành tuple (bất biến, dùng làm key được)
            res[tuple(count)].append(s)
        
        return list(res.values())


"""
Thuật toán:
1. Với mỗi từ, đếm số lần xuất hiện của từng ký tự 'a' → 'z'.
2. Biểu diễn tần suất này thành tuple (ví dụ: 'eat' → (1,0,0,...,1,...,1,...,0)).
3. Các anagram có tuple giống nhau → gom vào cùng một nhóm.
4. Trả về các nhóm này.

Ưu điểm: O(k) cho mỗi từ (k = độ dài từ), nhanh hơn so với O(k log k) ở cách 1.
"""
