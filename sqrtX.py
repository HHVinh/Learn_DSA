class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Trả về căn bậc hai nguyên (floor của sqrt(x)) bằng Binary Search.
        Ví dụ: x = 8 -> 2, x = 16 -> 4.
        Đặt đúng = x + 1 thay vì đúng = x để xử lý các trường hợp đầu vào đặc biệt như x = 0 và x = 1
        """
        
        l, r = 1, x + 1  
        while l < r:
            # Lấy giữa
            m = l + (r - l) // 2  
            
            # Nếu m*m > x thì kết quả nằm bên trái (nhỏ hơn m)
            if m * m > x:
                r = m
            else:
                # Nếu m*m <= x thì kết quả ít nhất là m
                l = m + 1
        
        # Khi vòng lặp kết thúc, l là số đầu tiên mà m*m > x
        # Nên căn bậc hai nguyên là l - 1
        return l - 1


# ================== Code chính để chạy trong VS Code ==================
if __name__ == "__main__":
    sol = Solution()
    
    # Nhập từ bàn phím
    x = int(input("Nhập số nguyên x: "))
    
    # Gọi hàm và in kết quả
    result = sol.mySqrt(x)
    print(f"Căn bậc hai nguyên của {x} là: {result}")
    
    # Thử thêm vài ví dụ mẫu để dễ so sánh
    test_cases = [0, 1, 4, 8, 15, 16, 17, 25, 26]
    print("\nMột vài ví dụ test thêm:")
    for num in test_cases:
        print(f"x = {num:2d}  =>  sqrt(x) = {sol.mySqrt(num)}")
