# Bài 122. Best Time to Buy and Sell Stock II
# Bạn có thể thắc mắc: "Nhỡ mua ngày 1 giá 1, đợi đến ngày 3 giá 10 thì lãi 9.
# Nếu bán ở ngày 2 giá 5 rồi mua lại giá 5 thì sao?

# Trong toán học: (B - A) + (C - B) = C - A

# Ví dụ: Giá tăng liên tục 1 -> 5 -> 10.
# Cách 1 (Hold to die): Mua 1, bán 10. Lãi = $9$.
# Cách 2 (Lướt sóng): Mua 1 bán 5 (lãi 4), rồi mua 5 bán 10 (lãi 5). 

# Tổng lãi = 4 + 5 = 9$. Kết quả như nhau. 
# Vì vậy, ta chỉ cần quan tâm đến các bước nhảy dương liền kề (adjacent difference), 
# cộng dồn chúng lại là ra kết quả tối ưu nhất mà không sợ bị "bán hớ".

class Solution:
    def maxProfit(self, prices):
        profit = 0                              # tổng lợi nhuận

        for i in range(1, len(prices)):        # duyệt từ ngày thứ 2
            if prices[i] > prices[i - 1]:      # nếu hôm nay giá cao hơn hôm qua
                profit += prices[i] - prices[i - 1]   # ăn phần chênh lệch

        return profit                           # trả về lợi nhuận tối đa


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))               # kết quả: 7
