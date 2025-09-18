class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0              # i bắt đầu từ cuối chuỗi, length để đếm độ dài từ cuối
        while i >= 0 and s[i] == ' ':          # bỏ qua các khoảng trắng ở cuối (nếu có)
            i -= 1
        while i >= 0 and s[i] != ' ':          # đếm độ dài ký tự cho đến khi gặp khoảng trắng hoặc hết chuỗi
            length += 1
            i -= 1
        return length                          # trả về độ dài từ cuối cùng

# ---- Chạy chương trình ----
if __name__ == "__main__":
    s = input("Nhập chuỗi: ")                  # yêu cầu người dùng nhập chuỗi
    sol = Solution()
    print("Độ dài từ cuối cùng là:", sol.lengthOfLastWord(s))
