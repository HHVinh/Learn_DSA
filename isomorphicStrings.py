class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Nếu độ dài 2 chuỗi khác nhau thì chắc chắn không thể isomorphic
        if len(s) != len(t):
            return False

        # mapST: ánh xạ ký tự từ s sang t
        # mapTS: ánh xạ ký tự từ t sang s (để kiểm tra ngược lại)
        mapST, mapTS = {}, {}

        # Duyệt qua từng ký tự theo chỉ số
        for i in range(len(s)):
            val1, val2 = s[i], t[i]  # val1: ký tự trong s, val2: ký tự trong t
            
            # Kiểm tra ánh xạ từ s -> t
            if val1 in mapST:
                # Nếu đã ánh xạ mà khác với ký tự t hiện tại -> không hợp lệ
                if mapST[val1] != val2:
                    return False
            else:
                # Nếu chưa có ánh xạ thì gán mới
                mapST[val1] = val2
            
            # Kiểm tra ánh xạ từ t -> s (chiều ngược lại)
            if val2 in mapTS:
                if mapTS[val2] != val1:
                    return False
            else:
                mapTS[val2] = val1

        # Nếu đi hết vòng lặp mà không mâu thuẫn thì hai chuỗi isomorphic
        return True


# ===========================
# Chạy thử để kiểm tra
# ===========================
if __name__ == "__main__":
    sol = Solution()

    # Ví dụ 1: "egg" -> "add" (true)
    print(sol.isIsomorphic("egg", "add"))  # True

    # Ví dụ 2: "foo" -> "bar" (false)
    print(sol.isIsomorphic("foo", "bar"))  # False

    # Ví dụ 3: "paper" -> "title" (true)
    print(sol.isIsomorphic("paper", "title"))  # True

    # Ví dụ 4: "badc" -> "baba" (false)
    print(sol.isIsomorphic("badc", "baba"))  # False
