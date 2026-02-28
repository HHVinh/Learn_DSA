# 122. Best Time to Buy and Sell Stock II
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        # not_hold: Lợi nhuận lớn nhất tính đến hiện tại nếu bạn KHÔNG CẦM cổ phiếu
        not_hold = 0 
        
        # hold: Lợi nhuận lớn nhất tính đến hiện tại nếu bạn ĐANG CẦM 1 cổ phiếu
        # Khởi tạo ngày đầu tiên (ngày 0): Nếu quyết định mua ngay, tài khoản của bạn bị âm một khoản bằng giá ngày 0
        hold = -prices[0] 
        
        # Bắt đầu duyệt từ ngày thứ 2 (index 1) trở đi
        for price in prices[1:]:
            # Lưu tạm lại lợi nhuận "không cầm cổ phiếu" của ngày hôm qua
            prev_not_hold = not_hold
            
            # CẬP NHẬT TRẠNG THÁI "KHÔNG CẦM CỔ PHIẾU" CHO HÔM NAY:
            # Chọn giá trị lớn nhất giữa 2 hành động:
            # 1. Nghỉ ngơi: Hôm qua cũng không cầm -> Lợi nhuận giữ nguyên (prev_not_hold)
            # 2. Chốt lời (Bán): Hôm qua đang cầm (hold), hôm nay bán lấy tiền (+ price) -> Lợi nhuận: hold + price
            not_hold = max(prev_not_hold, hold + price)
            
            # CẬP NHẬT TRẠNG THÁI "ĐANG CẦM CỔ PHIẾU" CHO HÔM NAY:
            # Chọn giá trị lớn nhất giữa 2 hành động:
            # 1. Giữ nguyên (Hold): Hôm qua đang cầm cổ phiếu rồi thì cứ cầm tiếp -> Lợi nhuận giữ nguyên (hold cũ)
            # 2. Bắt đáy (Mua): Hôm qua đang cầm tiền (prev_not_hold), hôm nay quyết định mua (- price) -> Lợi nhuận: prev_not_hold - price
            hold = max(hold, prev_not_hold - price)
            
        # Sau ngày cuối cùng, việc "bán hết thu tiền về" (not_hold) chắc chắn mang lại lợi nhuận cao hơn việc "vẫn ôm cổ phiếu" (hold)
        return not_hold
    
if __name__ == "__main__":    
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))