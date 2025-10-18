# Bài toán: Tìm cửa sổ con nhỏ nhất trong chuỗi s chứa tất cả ký tự của chuỗi t
# (bao gồm cả số lần xuất hiện của mỗi ký tự)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Nếu chuỗi t rỗng thì trả về chuỗi rỗng ngay
        if t == "":
            return ""

        # Bước 1: Đếm tần suất xuất hiện của từng ký tự trong t
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Biến lưu kết quả tốt nhất hiện tại
        res = [-1, -1]          # vị trí bắt đầu và kết thúc
        resLen = float("inf")   # độ dài nhỏ nhất (ban đầu là vô cực)

        # Duyệt qua tất cả vị trí bắt đầu i của chuỗi s
        for i in range(len(s)):
            countS = {}  # Đếm tần suất ký tự trong cửa sổ con hiện tại

            # Duyệt vị trí kết thúc j (tính từ i → cuối chuỗi)
            for j in range(i, len(s)):
                # Cập nhật tần suất ký tự s[j]
                countS[s[j]] = 1 + countS.get(s[j], 0)

                # Kiểm tra xem cửa sổ con s[i:j+1] có chứa đủ ký tự của t chưa
                flag = True
                for c in countT:
                    # Nếu thiếu ký tự nào trong t thì không đạt
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break

                # Nếu đủ ký tự, kiểm tra xem độ dài có nhỏ hơn kết quả tốt nhất chưa
                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        # Nếu tìm được cửa sổ con hợp lệ
        l, r = res
        if resLen != float("inf"):
            return s[l:r+1]
        else:
            return ""


# =============================
# Chạy thử chương trình
# =============================

if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print("Kết quả:", sol.minWindow(s, t))
