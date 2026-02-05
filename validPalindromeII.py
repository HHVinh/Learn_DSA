# 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Hàm kiểm tra chuỗi con s[l..r] có phải palindrome hay không
        def isPalindrome(l: int, r: int) -> bool:
            while l < r:                         # duyệt từ 2 đầu vào giữa
                if s[l] != s[r]:                # nếu 2 ký tự khác nhau
                    return False                # không phải palindrome
                l += 1                          # dịch trái sang phải
                r -= 1                          # dịch phải sang trái
            return True                         # duyệt xong mà không lỗi

        l = 0                                   # con trỏ trái
        r = len(s) - 1                          # con trỏ phải

        while l < r:                            # khi 2 con trỏ chưa gặp nhau
            if s[l] == s[r]:                    # nếu 2 ký tự giống nhau
                l += 1                          # tiếp tục vào trong
                r -= 1
            else:
                # gặp ký tự khác nhau → chỉ được phép xóa 1 ký tự
                # TH1: bỏ ký tự bên trái
                # TH2: bỏ ký tự bên phải
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)

        return True                             # chuỗi hợp lệ

if __name__ == "__main__":
    solution = Solution()

    print(solution.validPalindrome("abca"))   # True  (bỏ b hoặc c)
    print(solution.validPalindrome("racecar"))# True
    print(solution.validPalindrome("abc"))    # False
    print(solution.validPalindrome("deeee"))  # True