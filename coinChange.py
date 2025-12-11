from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Hàm trả về số lượng đồng xu ít nhất cần dùng để tạo ra 'amount'.
        Nếu không thể tạo ra, trả về -1.
        """

        # Tạo danh sách dp với kích thước amount + 1
        # dp[x] = số lượng xu ít nhất để tạo ra giá trị x
        # Khởi tạo tất cả phần tử = amount + 1 (coi như vô cực - không thể tạo)
        dp = [amount + 1] * (amount + 1)

        # dp[0] = 0 vì để tạo ra số tiền 0 thì không cần dùng đồng xu nào
        dp[0] = 0

        # Duyệt từng giá trị tiền từ 1 đến amount
        for a in range(1, amount + 1):

            # Thử từng loại đồng xu
            for c in coins:

                # Nếu dùng đồng xu c không vượt quá số tiền cần tạo
                if a - c >= 0:

                    # Cập nhật dp[a]:
                    # 1 + dp[a - c] nghĩa là dùng 1 xu c + số xu ít nhất để tạo ra (a - c)
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # Nếu dp[amount] vẫn là amount + 1 thì có nghĩa không thể tạo ra amount
        return dp[amount] if dp[amount] != amount + 1 else -1


# ------------------------
# Đoạn test để chạy trong VS Code
# ------------------------

if __name__ == "__main__":
    s = Solution()

    coins = [1, 2, 5]
    amount = 11

    result = s.coinChange(coins, amount)
    print(f"coins = {coins}, amount = {amount} → result = {result}")
