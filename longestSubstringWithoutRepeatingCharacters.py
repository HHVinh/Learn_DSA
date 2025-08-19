class Solution:
    # Cách 1: Dùng sliding window + set
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0                      # Biến lưu độ dài kết quả lớn nhất
        charSet = set()              # Set để lưu ký tự trong cửa sổ hiện tại (đảm bảo không trùng)
        l, n = 0, len(s)             # Con trỏ trái l và độ dài chuỗi n

        for r in range(n):           # Duyệt qua từng ký tự với con trỏ phải r
            # Nếu gặp ký tự trùng thì dịch con trỏ trái sang phải và xóa ký tự cũ
            while s[r] in charSet:   
                charSet.remove(s[l]) # Xóa ký tự tại con trỏ trái
                l += 1               # Dịch cửa sổ sang phải
            charSet.add(s[r])        # Thêm ký tự mới vào set
            res = max(res, r - l + 1)# Cập nhật kết quả (độ dài cửa sổ)
        return res
    
    # Cách 2: Dùng dict để lưu vị trí index cuối cùng của ký tự
    def lengthOfLongestSubstring2(self, s: str) -> int:
        mapDict = {}                 # Dictionary lưu {ký tự: vị trí index gần nhất}
        res = 0                      # Biến lưu kết quả
        l, n = 0, len(s)             # Con trỏ trái và độ dài chuỗi

        for r in range(n):           # Duyệt con trỏ phải r
            if s[r] in mapDict:      # Nếu ký tự đã xuất hiện
                # Dịch con trỏ trái l sang bên phải của vị trí cũ (nếu cần)
                l = max(l, mapDict[s[r]] + 1)
            mapDict[s[r]] = r        # Cập nhật vị trí mới nhất của ký tự
            res = max(res, r - l + 1)# Cập nhật độ dài lớn nhất
        return res

if __name__ == "__main__":
    s = input("Nhập chuỗi cần kiểm tra: ")
    sol = Solution()
    print("Độ dài substring không lặp (Cách 1 - set):", sol.lengthOfLongestSubstring(s))
    print("Độ dài substring không lặp (Cách 2 - dict):", sol.lengthOfLongestSubstring2(s))
