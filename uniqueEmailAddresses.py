from typing import List  # để dùng List[str]

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()  # dùng set để lưu email đã chuẩn hóa (unique)

        for strs in emails:
            temp = []                # danh sách lưu phần local name đã xử lý
            k = strs.index('@')      # tìm vị trí ký tự '@' trong email
            
            # duyệt từng ký tự trong email
            for i in range(len(strs)):
                if strs[i] == '@' or strs[i] == '+':
                    # gặp '@' hoặc '+' thì dừng xử lý local name
                    break
                if strs[i] != '.':
                    # bỏ qua dấu '.', còn lại thì thêm vào local name
                    temp.append(strs[i])
            
            # ghép lại: local name đã xử lý + phần domain name giữ nguyên
            newMail = ''.join(temp) + strs[k:]
            res.add(newMail)  # thêm vào set để tránh trùng
            
        return len(res)  # số lượng email khác nhau

# --- TEST ---
emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]

solution = Solution()
print(solution.numUniqueEmails(emails))  # Kết quả: 2
