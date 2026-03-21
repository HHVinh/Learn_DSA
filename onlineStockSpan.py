# 901. Online Stock Span

class StockSpanner:
    def __init__(self):
        # Stack sẽ lưu các tuple có dạng (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Chừng nào stack còn phần tử và giá ở đỉnh stack <= giá hiện tại
        while self.stack and self.stack[-1][0] <= price:
            # Cộng dồn span của ngày hôm trước vào span của ngày hôm nay
            # đồng thời loại bỏ phần tử đó khỏi stack
            span += self.stack.pop()[1]
            # Giả sử span = 1 và đỉnh stack đang là (75, 4). Khi đó:
            # Bước 1: self.stack.pop() lấy ra tuple là (75, 4) và xóa (75, 4) khỏi stack.
            # Bước 2: (75, 4)[1] sẽ rích xuất ra con số 4.
            # Bước 3: span += 4 => span = 5 và return 5.
            
        # Thêm giá hiện tại và tổng span vừa tính được vào stack
        self.stack.append((price, span))
        
        return span

if __name__ == "__main__":
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))  # Returns 1
    print(stockSpanner.next(80))   # Returns 1
    print(stockSpanner.next(60))   # Returns 1
    print(stockSpanner.next(70))   # Returns 2
    print(stockSpanner.next(60))   # Returns 1
    print(stockSpanner.next(75))   # Returns 4
    print(stockSpanner.next(85))   # Returns 6