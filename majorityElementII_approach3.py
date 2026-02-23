from collections import Counter
from typing import List

class Solution:
    # --- CÁCH 3: Dùng Hash Map (Dễ hiểu, Code ngắn) ---
    # Độ phức tạp: Time O(N), Space O(N)
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3                # Ngưỡng sàn (floor), cần lớn hơn số này
        counts = Counter(nums)            # Đếm tần suất xuất hiện của mọi số
        res = []
        
        for num, count in counts.items(): # Duyệt qua từng số đã đếm
            if count > threshold:         # Chỉ lấy số xuất hiện nhiều hơn n/3
                res.append(num)
        
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