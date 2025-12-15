from typing import List              # Dùng cho kiểu List[int]
from collections import deque        # Dùng deque để BFS hiệu quả


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:               # Nếu cần đổi 0 tiền
            return 0                  # Không cần đồng xu nào

        q = deque([0])                # Hàng đợi BFS, bắt đầu từ số tiền 0
        seen = [False] * (amount + 1) # Đánh dấu số tiền đã xét
        seen[0] = True                # Đã xét trạng thái 0
        res = 0                       # Số lượng đồng xu đã dùng (số tầng BFS)

        while q:                      # Khi hàng đợi còn phần tử
            res += 1                  # Sang tầng mới → thêm 1 đồng xu
            for _ in range(len(q)):   # Duyệt các trạng thái trong cùng tầng
                cur = q.popleft()     # Lấy số tiền hiện tại
                for coin in coins:    # Thử từng loại đồng xu
                    nxt = cur + coin  # Số tiền mới sau khi dùng coin

                    if nxt == amount: # Nếu đạt đúng số tiền cần đổi
                        return res    # Trả về số đồng xu nhỏ nhất

                    if nxt > amount or seen[nxt]:  # Nếu vượt quá hoặc đã xét
                        continue                   # Bỏ qua trạng thái này

                    seen[nxt] = True   # Đánh dấu đã xét
                    q.append(nxt)      # Thêm vào hàng đợi để xét tiếp

        return -1                     # Không thể đổi đúng số tiền


# -----------------------------
# PHẦN CHẠY THỬ TRONG VS CODE
# -----------------------------
if __name__ == "__main__":

    coins = [1, 2, 5]                 # Các loại đồng xu
    amount = 11                       # Số tiền cần đổi

    solution = Solution()
    result = solution.coinChange(coins, amount)

    print("Coins:", coins)
    print("Amount:", amount)
    print("Số đồng xu ít nhất:", result)
