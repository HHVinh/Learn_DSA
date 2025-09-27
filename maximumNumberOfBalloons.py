from collections import Counter  # Dùng để đếm số lần xuất hiện ký tự trong chuỗi

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Đếm số lần xuất hiện của từng ký tự trong chuỗi 'text'
        count_text = Counter(text)

        # Đếm số lần cần thiết của từng ký tự trong từ 'balloon'
        balloon = Counter("balloon")

        # Khởi tạo biến 'result' bằng độ dài chuỗi 'text'
        # Sau đó sẽ tìm giá trị nhỏ nhất trong quá trình tính toán
        result = len(text)
        
        # Duyệt qua từng ký tự cần có trong từ "balloon"
        for c in balloon:
            # Số lần có thể tạo ra ký tự 'c'
            # = số lần xuất hiện trong text // số lần cần thiết trong từ "balloon"
            result = min(result, count_text[c] // balloon[c])
        
        return result

# --- Đoạn code để chạy thử ---
if __name__ == "__main__":
    # Chuỗi đầu vào
    text = "loonbalxballpoon"
    
    solution = Solution()
    ketQua = solution.maxNumberOfBalloons(text)
    
    print("Số lần tối đa có thể tạo ra từ 'balloon' trong chuỗi là:", ketQua)
