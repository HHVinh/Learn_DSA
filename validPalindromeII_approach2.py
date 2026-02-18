# 680. Valid Palindrome II
# Nhược điểm kỹ thuật
# Tạo chuỗi mới → O(n), Reverse chuỗi → O(n), Tốn bộ nhớ hơn, Độ phức tạp thực tế:
# Thời gian: O(n) (vì slicing chỉ xảy ra 1 lần) Bộ nhớ: O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Khởi tạo 2 con trỏ đầu và cuối
        l, r = 0, len(s) - 1
        
        while l < r:
            # Nếu 2 ký tự giống nhau, tiếp tục co hẹp phạm vi
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Gặp cặp ký tự khác nhau!
                # Ta có 1 quyền xóa ký tự. Có 2 phương án:
                
                # Phương án 1: Xóa ký tự bên trái (s[l]). 
                # Kiểm tra đoạn còn lại từ l+1 đến r có đối xứng không.
                # Cú pháp s[l+1:r+1] lấy từ l+1 đến r (do Python slicing cận cuối là exclusive)
                skip_l = s[l+1 : r+1]
                
                # Phương án 2: Xóa ký tự bên phải (s[r]).
                # Kiểm tra đoạn còn lại từ l đến r-1 có đối xứng không.
                skip_r = s[l : r]
                
                # Chỉ cần 1 trong 2 phương án tạo ra chuỗi đối xứng là được
                return (skip_l == skip_l[::-1]) or (skip_r == skip_r[::-1])
        
        # Nếu chạy hết vòng lặp mà không gặp lỗi nào (hoặc chuỗi ban đầu đã đối xứng)
        return True
    
if __name__ == "__main__":
    solution = Solution()

    print(solution.validPalindrome("abca"))   # True  (bỏ b hoặc c)
    print(solution.validPalindrome("racecar"))# True
    print(solution.validPalindrome("abc"))    # False
    print(solution.validPalindrome("deeee"))  # True