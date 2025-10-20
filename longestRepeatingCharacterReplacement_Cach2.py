# Bài toán:
# Cho chuỗi s và số nguyên k.
# Bạn có thể thay tối đa k ký tự bất kỳ trong s để tạo ra chuỗi
# có nhiều ký tự giống nhau nhất liên tiếp.
# Hãy trả về độ dài lớn nhất của chuỗi con đó.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Biến lưu kết quả độ dài lớn nhất
        res = 0

        # Tạo tập hợp các ký tự có trong chuỗi s
        # (vì ta sẽ lần lượt chọn từng ký tự làm mục tiêu so sánh)
        charSet = set(s)

        # Duyệt qua từng ký tự trong chuỗi
        for c in charSet:
            count = 0  # đếm số ký tự c trong cửa sổ hiện tại
            l = 0      # con trỏ trái

            # Duyệt qua từng vị trí trong chuỗi (con trỏ phải)
            for r in range(len(s)):
                # Nếu ký tự tại r trùng với c, tăng count
                if s[r] == c:
                    count += 1

                # Nếu số ký tự khác c trong cửa sổ lớn hơn k,
                # thì ta cần dịch con trỏ trái l sang phải để thu nhỏ cửa sổ
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                # Cập nhật độ dài lớn nhất
                res = max(res, r - l + 1)

        return res


# =============================
# PHẦN MAIN ĐỂ CHẠY THỬ TRONG VS CODE
# =============================

if __name__ == "__main__":
    # Nhập chuỗi và giá trị k từ người dùng
    s = input("Nhập chuỗi s: ")
    k = int(input("Nhập số k: "))

    # Tạo đối tượng Solution
    sol = Solution()

    # Gọi hàm và in kết quả
    result = sol.characterReplacement(s, k)
    print("Độ dài chuỗi con dài nhất có thể tạo ra là:", result)
