from typing import List  # Thư viện dùng cho kiểu dữ liệu List (không bắt buộc nhưng nên có)

class Solution:
    def countSubstrings(self, s: str) -> int:  # Hàm đếm số chuỗi con đối xứng

        def manacher(s):  # Thuật toán Manacher để tìm bán kính palindrome
            t = '#' + '#'.join(s) + '#'  # Chèn ký tự # để xử lý cả chuỗi chẵn và lẻ
            n = len(t)  # Lấy độ dài chuỗi mới
            p = [0] * n  # Mảng lưu bán kính đối xứng tại mỗi vị trí
            l, r = 0, 0  # L = biên trái, R = biên phải của palindrome lớn nhất hiện tại

            for i in range(n):  # Duyệt từng ký tự trong chuỗi mới
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0  # Tận dụng kết quả cũ nếu nằm trong vùng palindrome

                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0   # Kiểm tra không vượt biên
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):  # So sánh 2 ký tự đối xứng
                    p[i] += 1  # Mở rộng bán kính đối xứng

                if i + p[i] > r:  # Nếu palindrome mới vượt biên phải cũ
                    l, r = i - p[i], i + p[i]  # Cập nhật biên trái và phải

            return p  # Trả về mảng bán kính palindrome

        p = manacher(s)  # Gọi thuật toán Manacher
        res = 0  # Biến lưu tổng số chuỗi đối xứng

        for i in p:  # Duyệt từng bán kính trong mảng p
            res += (i + 1) // 2  # Quy đổi sang số palindrome thực trong chuỗi ban đầu

        return res  # Trả về kết quả cuối cùng


# ========================== PHẦN CHẠY THỬ ==========================

if __name__ == "__main__":  # Đảm bảo file chạy trực tiếp thì mới thực thi
    s = input("Nhập chuỗi: ")  # Nhập chuỗi từ bàn phím
    sol = Solution()  # Tạo đối tượng Solution
    result = sol.countSubstrings(s)  # Gọi hàm đếm palindrome
    print("Số chuỗi con đối xứng là:", result)  # In kết quả
