from collections import defaultdict
from typing import List

class Solution:
    # --- CÁCH 2: Boyer-Moore Tổng Quát (Dùng Dict + Continue) ---
    # Ưu điểm: Code linh hoạt, dùng được cho bài toán tìm số > 1/k
    # Nhược điểm: Chậm hơn Cách 2 một chút do quản lý Dict
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)         # Tạo dict đếm ứng viên
        
        # Giai đoạn 1: Tìm ứng viên (Lọc)
        for num in nums:
            count[num] += 1              # Thêm số vào danh sách
            
            if len(count) <= 2:          # Nếu danh sách chưa đầy (<= 2 ứng viên)
                continue                 # Giữ nguyên, đi tiếp vòng lặp (SKIP đoạn dưới)
            
            # Nếu danh sách bị đầy (lên 3 số), thực hiện "Triệt tiêu"
            new_count = defaultdict(int) # Tạo dict mới để lọc số
            for k, v in count.items():   # Duyệt qua các ứng viên hiện có
                if v > 1:                # Nếu số lượng > 1 (trừ đi 1 vẫn sống)
                    new_count[k] = v - 1 # Giảm 1 đơn vị và giữ lại
            count = new_count            # Cập nhật lại danh sách ứng viên
            
        # Giai đoạn 2: Kiểm tra lại (Count lần 2) - Bắt buộc
        res = []
        threshold = len(nums) // 3       # Ngưỡng sàn (> n/3)
        for num in count:                # Duyệt qua các ứng viên còn sót lại
            if nums.count(num) > threshold: # Đếm lại thực tế trong mảng gốc
                res.append(num)          # Nếu thỏa mãn thì thêm vào kết quả
                
        return res
    
# --- PHẦN MAIN ĐỂ CHẠY THỬ ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test case mẫu
    test_cases = [
        [3, 2, 3],                  # Kỳ vọng: [3]
        [1],                        # Kỳ vọng: [1]
        [1, 2],                     # Kỳ vọng: [1, 2]
        [1, 2, 3],                  # Kỳ vọng: [] (Không ai > 1/3) (1/3 của 3 là 1, cần > 1 tức là 2)
        [2, 2, 1, 1, 1, 2, 2]       # Kỳ vọng: [2, 1]
    ]

    print("--- CHẠY THỬ NGHIỆM ---")
    for idx, nums in enumerate(test_cases):
        print(f"\nTest {idx + 1}: Input = {nums}")
        
        res = sol.majorityElement(nums)
        print(f"  -> Cách Hash Map:    {res}")
        