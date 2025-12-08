from typing import List  # Thư viện hỗ trợ kiểu dữ liệu (không bắt buộc nhưng nên có)

class Solution:
    def numDecodings(self, s: str) -> int:  # Hàm đếm số cách giải mã chuỗi số
        dp = 0    # dp: số cách giải mã tại vị trí i hiện tại
        dp2 = 0   # dp2: số cách giải mã tại vị trí i + 2
        dp1 = 1   # dp1: số cách giải mã tại vị trí i + 1 (ban đầu là 1 vì chuỗi rỗng có 1 cách)

        for i in range(len(s) - 1, -1, -1):  # Duyệt chuỗi từ phải sang trái
            if s[i] == "0":  # Nếu ký tự hiện tại là '0'
                dp = 0  # Không có cách giải mã hợp lệ
            else:
                dp = dp1  # Kế thừa số cách giải mã của vị trí kế tiếp

            if i + 1 < len(s) and (s[i] == "1" or   # Nếu 2 chữ số tạo thành số từ 10 → 19
               s[i] == "2" and s[i + 1] in "0123456"  # Hoặc từ 20 → 26
            ):
                dp += dp2  # Cộng thêm số cách giải mã của vị trí i + 2

            dp, dp1, dp2 = 0, dp, dp1  # Dịch chuyển trạng thái: dp2 <- dp1, dp1 <- dp

        return dp1  # Trả về số cách giải mã tại vị trí đầu chuỗi


# ========================== PHẦN CHẠY THỬ ==========================

if __name__ == "__main__":  # Chỉ chạy khi file được chạy trực tiếp
    s = input("Nhập chuỗi mã hóa (vd: 226): ")  # Nhập chuỗi số từ bàn phím
    sol = Solution()  # Tạo object Solution
    result = sol.numDecodings(s)  # Gọi hàm đếm số cách giải mã
    print("Số cách giải mã là:", result)  # In kết quả
