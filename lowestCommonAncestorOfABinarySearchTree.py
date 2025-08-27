# Định nghĩa cấu trúc một node trong cây nhị phân
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Tìm tổ tiên chung gần nhất (Lowest Common Ancestor - LCA)
        trong Binary Search Tree (BST).
        Ý tưởng:
        - Nếu cả p và q đều lớn hơn node hiện tại -> đi sang phải
        - Nếu cả p và q đều nhỏ hơn node hiện tại -> đi sang trái
        - Ngược lại -> node hiện tại chính là LCA
        """
        res = root
        while res:
            if p.val > res.val and q.val > res.val:
                res = res.right  # cả p và q ở bên phải
            elif p.val < res.val and q.val < res.val:
                res = res.left   # cả p và q ở bên trái
            else:
                return res       # chia đôi đường hoặc trùng => đây là LCA
        return None


# Hàm phụ để xây BST từ danh sách level-order (LeetCode style)
def build_tree_from_list(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


# =============================
# Test thử
# =============================
if __name__ == "__main__":
    # Ví dụ 1: Cây [3,1,8,null,null,5,10,4,6,9,11]
    values = [3,1,8,None,None,5,10,4,6,9,11]
    root = build_tree_from_list(values)

    p = TreeNode(9)
    q = TreeNode(11)

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val if lca else None}")

    # Ví dụ 2: Cây [6,2,8,0,4,7,9,None,None,3,5], p=2, q=8
    values2 = [6,2,8,0,4,7,9,None,None,3,5]
    root2 = build_tree_from_list(values2)

    p2 = TreeNode(2)
    q2 = TreeNode(8)
    lca2 = sol.lowestCommonAncestor(root2, p2, q2)
    print(f"LCA of {p2.val} and {q2.val} is: {lca2.val if lca2 else None}")
