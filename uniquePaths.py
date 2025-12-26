class SolutionDP1D:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[j] = số cách đi đến cột j của hàng hiện tại
        dp = [1] * n   # hàng đầu tiên chỉ có 1 cách

        # Duyệt từ hàng thứ 2 trở đi
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]  # từ trên + từ trái

        return dp[-1]

class SolutionDP2D:
    def uniquePaths(self, m: int, n: int) -> int:
        # Tạo bảng dp gồm m hàng, n cột
        # Mỗi ô ban đầu = 1
        dp = [[1] * n for _ in range(m)]

        # Duyệt từ hàng thứ 2 (i = 1)
        for i in range(1, m):
            # Duyệt từ cột thứ 2 (j = 1)
            for j in range(1, n):
                # Số cách tới ô (i,j)
                # = số cách từ trên + số cách từ trái
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Ô cuối cùng là kết quả
        return dp[m - 1][n - 1]

# =========================
# Test chạy VS Code
# =========================
if __name__ == "__main__":
    sol = SolutionDP1D()
    print("DP 1D:", sol.uniquePaths(3, 7))  # 28

    sol = SolutionDP2D()
    print("DP 2D:", sol.uniquePaths(3, 7))  # 28
