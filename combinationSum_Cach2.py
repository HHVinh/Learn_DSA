from typing import List  # Dùng để gợi ý kiểu dữ liệu (List[int], List[List[int]])

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  # Danh sách kết quả chứa các tổ hợp hợp lệ

        # Hàm đệ quy DFS (duyệt sâu)
        # i: chỉ số hiện tại trong danh sách nums
        # cur: danh sách hiện tại các số được chọn
        # total: tổng các số trong cur
        def dfs(i, cur, total):
            # Nếu tổng hiện tại đúng bằng target → thêm bản sao cur vào kết quả
            if total == target:
                res.append(cur.copy())
                return
            
            # Nếu đã xét hết các số hoặc tổng vượt target → dừng nhánh này
            if i >= len(nums) or total > target:
                return

            # --- Nhánh 1: chọn nums[i] ---
            cur.append(nums[i])  # thêm phần tử hiện tại vào tổ hợp
            # Gọi lại dfs tại cùng chỉ số i (vì có thể dùng lại số này)
            dfs(i, cur, total + nums[i])
            cur.pop()  # bỏ phần tử vừa thêm để quay lại trạng thái trước (backtrack)

            # --- Nhánh 2: bỏ qua nums[i] ---
            dfs(i + 1, cur, total)  # sang phần tử tiếp theo

        # Bắt đầu đệ quy từ chỉ số 0, tổ hợp rỗng, tổng 0
        dfs(0, [], 0)

        return res  # Trả về tất cả các tổ hợp tìm được


# -----------------------------
# HÀM MAIN ĐỂ CHẠY TRONG VS CODE
# -----------------------------
def main():
    # Nhập danh sách số
    # Ví dụ: nhập 2 3 6 7 rồi nhấn Enter
    nums = list(map(int, input("Nhập các số trong danh sách (cách nhau bởi dấu cách): ").split()))
    
    # Nhập giá trị target
    target = int(input("Nhập giá trị target: "))

    # Tạo đối tượng Solution và gọi hàm combinationSum
    solution = Solution()
    result = solution.combinationSum(nums, target)

    # In kết quả
    print("\nCác tổ hợp có tổng bằng", target, "là:")
    for combo in result:
        print(combo)


# Chạy chương trình chính khi file được chạy trực tiếp
if __name__ == "__main__":
    main()
