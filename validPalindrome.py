class Solution:
    # Cách 1: Tạo chuỗi mới rồi so sánh với bản đảo ngược
    def isPalindrome(self, s: str) -> bool:
        newStr = ''                   # Tạo chuỗi rỗng để chứa ký tự hợp lệ
        for c in s:                   # Duyệt từng ký tự trong chuỗi gốc
            if c.isalnum():           # Nếu là chữ hoặc số
                newStr += c.lower()   # Đưa về chữ thường và nối vào chuỗi mới
        return newStr == newStr[::-1] # So sánh chuỗi với bản đảo ngược của nó

    # Cách 2: Dùng 2 con trỏ (trái - phải) và isalnum()
    def isPalindrome2(self, s: str) -> bool:
        l = 0                         # Con trỏ trái (bắt đầu từ đầu chuỗi)
        r = len(s)-1                  # Con trỏ phải (bắt đầu từ cuối chuỗi)
        while l < r:                  # Lặp cho tới khi 2 con trỏ gặp nhau
            while l < r and not s[l].isalnum():  # Nếu ký tự trái không hợp lệ -> bỏ qua
                l += 1
            while r > l and not s[r].isalnum():  # Nếu ký tự phải không hợp lệ -> bỏ qua
                r -= 1
            if s[l].lower() != s[r].lower():     # So sánh ký tự (không phân biệt hoa/thường)
                return False
            l += 1                  # Tiến con trỏ trái
            r -= 1                  # Lùi con trỏ phải
        return True                 # Nếu hết vòng lặp mà không sai -> là palindrome
    
    # Cách 3: Dùng 2 con trỏ (trái - phải) và check() thay cho isalnum()
    # Hàm tự viết để kiểm tra ký tự có phải chữ hoặc số
    def check(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or   # Ký tự từ A-Z
                ord('a') <= ord(c) <= ord('z') or   # Ký tự từ a-z
                ord('0') <= ord(c) <= ord('9'))     # Hoặc là số 0-9

    def isPalindrome3(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.check(s[l]):   # Nếu ký tự trái không hợp lệ -> bỏ qua
                l += 1
            while r > l and not self.check(s[r]):   # Nếu ký tự phải không hợp lệ -> bỏ qua
                r -= 1
            if s[l].lower() != s[r].lower():        # So sánh ký tự
                return False
            l, r = l+1, r-1
        return True

sol = Solution()
s = input("Nhập chuỗi cần kiểm tra: ")

print("Cách 1 (alphaNum):", sol.isPalindrome(s))
print("Cách 2 (isalnum):", sol.isPalindrome2(s))
print("Cách 3 (buildStr):", sol.isPalindrome3(s))