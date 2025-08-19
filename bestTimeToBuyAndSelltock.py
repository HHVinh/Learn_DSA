class Solution:
    def bestTimeBuyAndSellStock(self, prices: list[int]) -> int:
        res = 0                # Lưu lợi nhuận lớn nhất
        l, r = 0, 1            # l: ngày mua, r: ngày bán
        n = len(prices)        # Độ dài danh sách giá
        while r < n:           # Lặp đến khi r ra ngoài mảng
            if prices[l] < prices[r]:                      # Nếu giá bán > giá mua
                res = max(res, prices[r] - prices[l])      # Cập nhật lợi nhuận lớn nhất
            else:
                l = r             # Nếu giá bán <= giá mua, chọn giá mua mới
            r += 1                # Dịch ngày bán sang phải
        return res                # Trả về lợi nhuận lớn nhất
    
    def bestTimeBuyAndSellStock2(self, prices: list[int]) -> int:
        res = 0                   # Lưu lợi nhuận lớn nhất
        priceMin = prices[0]      # Giá thấp nhất tính đến hiện tại
        for price in prices:      
            res = max(res, price - priceMin)   # Nếu bán hôm nay, lợi nhuận có thể tăng
            priceMin = min(priceMin, price)    # Cập nhật giá mua rẻ nhất
        return res                 # Trả về lợi nhuận lớn nhất

    def bestTimeBuyAndSellStock3(self, prices: list[int]) -> int:
        hold = -prices[0]          # Trạng thái "đang giữ cổ phiếu" (mua ngày đầu) -> lợi nhuận âm
        notHold = 0                # Trạng thái "không giữ cổ phiếu" -> lợi nhuận ban đầu = 0
        for price in prices:
            hold = max(hold, -price)           # Giữ nguyên cổ phiếu hoặc mua tại giá hôm nay
            notHold = max(notHold, hold + price)  # Giữ nguyên trạng thái hoặc bán hôm nay
        return notHold             # Kết quả: lợi nhuận khi không còn giữ cổ phiếu

sol = Solution()
prices = list(map(int, input("Nhập các giá ngẫu nhiên cách nhau khoảng trắng: ").split()))  
print("Cách 1: ")
print(sol.bestTimeBuyAndSellStock(prices))    
print("\nCách 2: ")
print(sol.bestTimeBuyAndSellStock2(prices))   
print("\nCách 3 (State Machine): ")
print(sol.bestTimeBuyAndSellStock3(prices))   
