class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s: str):
            t = "#" + "#".join(s) + "#" # Ví dụ: "abba" -> "#a#b#b#a#"
            n = len(t) # Số phần tử của chuỗi mới
            p = [0] * n # p[i] = số bước có thể mở rộng đối xứng từ vị trí i
            l, r = 0, 0 # l = biên trái, r = biên phải của palindrome lớn nhất hiện tại

            for i in range(n): # DUYỆT TỪNG VỊ TRÍ i TRONG t
                if i < r: # NẾU i NẰM TRONG VÙNG ĐỐI XỨNG [l, r]
                    mirror = l + (r - i) # Vị trí đối xứng của i qua tâm hiện tại
                    p[i] = min(r - i, p[mirror]) # Sao chép giá trị đối xứng nhưng không vượt ra ngoài r
                else:
                    p[i] = 0 # Nếu i nằm ngoài vùng đối xứng

                while ( # MỞ RỘNG THẬT SỰ SANG TRÁI VÀ PHẢI
                    i + p[i] + 1 < n and              # Không vượt biên phải
                    i - p[i] - 1 >= 0 and             # Không vượt biên trái
                    t[i + p[i] + 1] == t[i - p[i] - 1]  # Hai ký tự đối xứng phải bằng nhau
                ):
                    p[i] += 1

                if i + p[i] > r: # NẾU PALINDROME TẠI i LỚN HƠN CÁI CŨ
                    l = i - p[i] # Cập nhật lại biên trái và biên phải
                    r = i + p[i]
            return p # Trả về mảng bán kính đối xứng
        
        p = manacher(s)
        resLen = 0  # resLen = bán kính lớn nhất
        center_idx = 0 # center_idx = vị trí trung tâm của palindrome dài nhất

        for i in range(len(p)):
            if p[i] > resLen:
                resLen = p[i]
                center_idx = i

        start_index = (center_idx - resLen) // 2 # Công thức đổi chỉ số từ t về s
        return s[start_index : start_index + resLen] # Cắt chuỗi kết quả từ s


# ================================
# PHẦN CHẠY CHƯƠNG TRÌNH TRONG VS CODE
# ================================
if __name__ == "__main__":
    s = input("Nhập chuỗi: ")

    solution = Solution()
    result = solution.longestPalindrome(s)

    print("Chuỗi đối xứng dài nhất là:", result)
