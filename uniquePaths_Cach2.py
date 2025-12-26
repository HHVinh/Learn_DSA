class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Nếu m > n thì hoán đổi
        # Mục đích: luôn lặp theo số nhỏ hơn để giảm số phép tính
        # (không làm thay đổi kết quả toán học)
        if m > n:
            m, n = n, m

        # Tổng số bước robot phải đi:
        # (m - 1) bước xuống + (n - 1) bước sang phải
        N = m + n - 2

        # res dùng để lưu kết quả tổ hợp C(N, m-1)
        # Bắt đầu từ 1 để nhân dần
        res = 1

        # Tính tổ hợp theo công thức nhân dần:
        # C(N, m-1) = N/1 * (N-1)/2 * ... * (N-(m-2))/(m-1)
        for i in range(1, m):
            # Nhân trước, chia sau để:
            # - Không bị sai số
            # - res luôn là số nguyên
            res = res * (N - i + 1) // i
        
        # Kết quả cuối cùng là số đường đi khác nhau
        return res



# =========================
# Test
# =========================
if __name__ == "__main__":
    sol = Solution()
    print("Your code:", sol.uniquePaths(3, 7))  # 28
