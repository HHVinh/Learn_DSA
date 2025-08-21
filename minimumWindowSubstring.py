class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":  # nếu t rỗng thì không có cửa sổ nào
            return ""

        countT, window = {}, {}  # countT: đếm ký tự trong t, window: đếm ký tự trong cửa sổ hiện tại
        for c in t:
            countT[c] = 1 + countT.get(c, 0)  # tăng số lần xuất hiện ký tự c trong t
        
        have, need = 0, len(countT)  # have: số ký tự thỏa trong window, need: số ký tự cần đủ
        res, resLen = [-1, -1], float("infinity")  # res: vị trí [l, r] tốt nhất, resLen: độ dài nhỏ nhất
        l = 0  # con trỏ trái
        for r in range(len(s)):  # duyệt con trỏ phải
            c = s[r]
            window[c] = 1 + window.get(c, 0)  # tăng số lần xuất hiện ký tự c trong window

            if c in countT and window[c] == countT[c]:  # nếu số lượng c trong window đủ với countT
                have += 1

            while have == need:  # khi window đã chứa đủ tất cả ký tự trong t
                if (r - l + 1) < resLen:  # nếu cửa sổ nhỏ hơn resLen hiện tại
                    res = [l, r]  # cập nhật vị trí cửa sổ
                    resLen = r - l + 1  # cập nhật độ dài nhỏ nhất

                window[s[l]] -= 1  # giảm số lượng ký tự ở đầu cửa sổ
                if s[l] in countT and window[s[l]] < countT[s[l]]:  # nếu thiếu ký tự cần
                    have -= 1
                l += 1  # dịch trái sang phải
        l, r = res
        resLen = r - l + 1

        return s[l : r + 1] if resLen != float("infinity") else ""  # trả về chuỗi con nhỏ nhất hoặc ""
    
sol = Solution()
s = input("Nhập chuỗi s: ")  # chuỗi gốc
t = input("Nhập chuỗi t: ")  # chuỗi cần tìm trong s

print(sol.minWindow(s, t))  # in kết quả
