# Bài 122

class Solution:
    def maxProfit(self, prices):
        dp0 = 0                    # không cầm cổ phiếu
        dp1 = -prices[0]           # đang cầm cổ phiếu

        for i in range(1, len(prices)):
            temp = dp0 # Lưu lại trạng thái cầm tiền của ngày hôm qua
            dp0 = max(dp0, dp1 + prices[i]) # Cập nhật trạng thái Cầm tiền (Bán hoặc Nghỉ)
            dp1 = max(dp1, temp - prices[i]) # Cập nhật trạng thái Giữ cổ (Giữ tiếp hoặc Mua mới)

        return dp0


    def maxProfit2DP(self, prices):
        n = len(prices)
        dp0 = [0] * n                    # dp0[i]: không cầm cổ phiếu
        dp1 = [0] * n                    # dp1[i]: đang cầm cổ phiếu

        dp0[0] = 0
        dp1[0] = -prices[0]

        for i in range(1, n):

            dp0[i] = max(
                dp0[i - 1], # hôm qua không cầm, hôm nay vẫn không làm gì
                dp1[i - 1] + prices[i]) # hôm qua cầm, hôm nay bán            

            dp1[i] = max(
                dp1[i - 1], # hôm qua cầm, hôm nay giữ
                dp0[i - 1] - prices[i]) # hôm qua không cầm, hôm nay mua

        return dp0[-1]


if __name__ == "__main__":
    prices = [1, 3, 2, 4]
    print(Solution().maxProfit(prices))   # 4
    print(Solution().maxProfit2DP(prices))   # 4
