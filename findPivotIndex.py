class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumAll = sum(nums)  # Tính tổng toàn bộ dãy
        sumLeft = 0  # Biến lưu tổng của các phần tử bên trái
        
        # Duyệt qua từng phần tử trong dãy
        for i in range(len(nums)):
            # Tính tổng bên phải = tổng toàn bộ - tổng bên trái - phần tử hiện tại
            sumRight = sumAll - sumLeft - nums[i]
            
            # Nếu tổng bên trái == tổng bên phải thì i là pivot index
            if sumLeft == sumRight:
                return i  
            
            # Cập nhật tổng bên trái trước khi chuyển sang phần tử tiếp theo
            sumLeft += nums[i]
        
        # Nếu duyệt hết mà không tìm được, trả về -1
        return -1


# --- Chạy thử ---
if __name__ == "__main__":
    s = Solution()
    
    nums = [1, 7, 3, 6, 5, 6]
    print(s.pivotIndex(nums))  # Output: 3 (vì bên trái và bên phải index 3 có tổng bằng nhau)
    
    nums = [1, 2, 3]
    print(s.pivotIndex(nums))  # Output: -1 (không có pivot index nào)
    
    nums = [2, 1, -1]
    print(s.pivotIndex(nums))  # Output: 0 (bên trái rỗng nên tổng = 0, bên phải cũng = 0)
