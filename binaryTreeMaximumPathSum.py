from typing import Optional
# Định nghĩa một node trong cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # res[0] dùng để lưu tổng đường đi lớn nhất tìm thấy
        # Dùng list vì biến trong list có thể thay đổi được trong hàm dfs
        res = [root.val]

        def dfs(root):
            if not root:
                # Nếu node rỗng thì không đóng góp gì, trả về 0
                return 0

            # Tính tổng lớn nhất của nhánh trái và nhánh phải
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Nếu một nhánh âm thì bỏ qua (chọn 0 để không làm giảm tổng)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Xem xét đường đi "nằm giữa" đi qua node hiện tại
            # (nhánh trái + node hiện tại + nhánh phải)
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Khi trả kết quả về cho cha, chỉ được chọn 1 nhánh (trái hoặc phải)
            return root.val + max(leftMax, rightMax)

        # Bắt đầu duyệt từ gốc
        dfs(root)

        # Trả về kết quả cuối cùng
        return res[0]


# ------------------ Chạy thử ------------------
if __name__ == "__main__":
    # Tạo cây ví dụ:
    #         -10
    #         /  \
    #        9    20
    #            /  \
    #           15   7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    sol = Solution()
    print("Đường đi lớn nhất trong cây là:", sol.maxPathSum(root))
    # Kết quả mong đợi: 42
