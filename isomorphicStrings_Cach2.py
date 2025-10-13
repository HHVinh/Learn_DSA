class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Nếu hai chuỗi không cùng độ dài => chắc chắn không đẳng cấu
        if len(s) != len(t):
            return False

        # mapping: dùng để lưu ánh xạ từ ký tự của s sang ký tự của t
        mapping = {}

        # Duyệt từng vị trí ký tự trong chuỗi
        for i in range(len(s)):
            char_s = s[i]  # Ký tự trong chuỗi s
            char_t = t[i]  # Ký tự tương ứng trong chuỗi t

            # Nếu ký tự s[i] chưa được ánh xạ
            if char_s not in mapping:
                # Kiểm tra ký tự t[i] đã được ánh xạ từ ký tự khác trong s chưa
                if char_t not in mapping.values():
                    # Nếu chưa, tạo ánh xạ mới
                    mapping[char_s] = char_t
                else:
                    # Nếu rồi => có 2 ký tự khác của s cùng ánh xạ đến 1 ký tự của t => sai
                    return False
            else:
                # Nếu s[i] đã từng ánh xạ => kiểm tra có đúng ký tự tương ứng t[i] không
                if mapping[char_s] != char_t:
                    return False  # Nếu khác => sai (một ký tự s ánh xạ sang hai ký tự t khác nhau)

        # Nếu duyệt hết mà không sai => hai chuỗi là đẳng cấu
        return True


# --- Kiểm thử ---
solution = Solution()
print(solution.isIsomorphic("egg", "add"))   # ✅ True (e->a, g->d)
print(solution.isIsomorphic("foo", "bar"))   # ❌ False
print(solution.isIsomorphic("paper", "title"))  # ✅ True
print(solution.isIsomorphic("ab", "aa"))     # ❌ False
