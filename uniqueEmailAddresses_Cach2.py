# Mục tiêu: Đếm số địa chỉ email duy nhất sau khi chuẩn hoá theo quy tắc:
#   - Trong phần "local" (trước @):
#       + Bỏ qua tất cả dấu '.'
#       + Bỏ phần sau dấu '+'
#   - Phần "domain" (sau @) giữ nguyên

from typing import List  # thêm để VS Code hiểu kiểu dữ liệu List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Sử dụng set để lưu các email duy nhất sau khi chuẩn hoá
        res = set()

        # Duyệt qua từng email trong danh sách
        for e in emails:
            # Tách phần "local" (trước @) và "domain" (sau @)
            # Tham số thứ hai = 1 để chỉ tách tại ký tự '@' đầu tiên
            local, domain = e.split('@', 1)

            # Xử lý phần local:
            # 1️⃣ Tách tại dấu '+' (nếu có) -> chỉ lấy phần trước dấu '+'
            # 2️⃣ Xóa hết dấu '.' trong phần local
            local = local.split('+', 1)[0].replace('.', '')

            # Ghép lại email đã chuẩn hoá
            new_email = local + '@' + domain

            # Thêm vào set (set sẽ tự loại bỏ trùng lặp)
            res.add(new_email)

        # Trả về số lượng email duy nhất sau khi xử lý
        return len(res)


# 🧩 --- Ví dụ chạy thử ---
if __name__ == "__main__":
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]

    sol = Solution()
    print("Số lượng email duy nhất:", sol.numUniqueEmails(emails))
