from typing import List
class Solution:
    # --- CÁCH 1: Boyer-Moore Voting (Tối ưu bộ nhớ nhất) ---
    # Độ phức tạp: Time O(N), Space O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        # Giai đoạn 1: Tìm 2 ứng viên tiềm năng
        cand1, cand2 = None, None         # Hai ghế trống cho 2 ứng viên
        count1, count2 = 0, 0             # Số phiếu (lính) của mỗi phe

        for num in nums:
            if cand1 == num:              # Nếu gặp quân phe 1
                count1 += 1               # Tăng lính phe 1
            elif cand2 == num:            # Nếu gặp quân phe 2
                count2 += 1               # Tăng lính phe 2
            elif count1 == 0:             # Nếu ghế 1 đang trống (hoặc lính chết hết)
                cand1, count1 = num, 1    # Chiếm ghế 1
            elif count2 == 0:             # Nếu ghế 2 đang trống
                cand2, count2 = num, 1    # Chiếm ghế 2
            else:                         # Gặp kẻ thứ 3 (khác cả 2 phe trên)
                count1 -= 1               # Phe 1 mất 1 lính (triệt tiêu)
                count2 -= 1               # Phe 2 mất 1 lính (triệt tiêu)

        # Giai đoạn 2: Kiểm tra lại (Bắt buộc)
        res = []
        n = len(nums)
        threshold = n // 3
        
        # Đếm lại số lần thực tế của 2 ứng viên còn sống sót
        if nums.count(cand1) > threshold: res.append(cand1)
        if nums.count(cand2) > threshold:
            if cand2 != cand1:            # Tránh trường hợp cand1 trùng cand2
                res.append(cand2)
                
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
        print(f"  -> Cách Boyer-Moore: {res}")