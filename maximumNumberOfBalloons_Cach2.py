# Bài toán: Đếm xem có thể tạo được bao nhiêu lần từ "balloon" từ chuỗi text

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Tạo dictionary để đếm số lần xuất hiện của các ký tự trong từ "balloon"
        # Chỉ cần 5 ký tự: b, a, l, o, n
        countT = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        # Duyệt qua từng ký tự trong chuỗi text
        for c in text:
            # Nếu ký tự nằm trong từ "balloon" thì tăng số đếm tương ứng
            if c in countT:
                countT[c] += 1

        # Trong từ "balloon", chữ 'l' và 'o' xuất hiện 2 lần
        # Nên ta chia đôi số lần đếm của chúng để tính đúng số lượng từ "balloon" có thể tạo được
        countT['l'] //= 2
        countT['o'] //= 2

        # Số lượng từ "balloon" tạo được phụ thuộc vào ký tự nào xuất hiện ít nhất
        # Nên ta lấy giá trị nhỏ nhất trong các số đếm
        return min(countT.values())


# --- ĐOẠN KIỂM TRA CHẠY THỬ ---
text = "loonbalxballpoon"  # ví dụ mẫu
solution = Solution()
print(solution.maxNumberOfBalloons(text))  # Kết quả mong đợi: 2
