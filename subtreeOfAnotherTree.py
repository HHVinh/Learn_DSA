class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # ---------------------- Cách 1: Dùng so sánh trực tiếp ----------------------
    def isSubtree1(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        Kiểm tra subRoot có phải là subtree của root bằng cách duyệt DFS
        và gọi hàm so sánh sameTree.
        """
        if not subRoot:   # Nếu subRoot rỗng => luôn là subtree
            return True
        if not root:      # Nếu root rỗng mà subRoot không rỗng => False
            return False
        
        # Nếu tìm được node khớp hoàn toàn
        if self.sameTree(root, subRoot):
            return True

        # Duyệt tiếp xuống 2 nhánh con
        return (self.isSubtree1(root.left, subRoot) or 
                self.isSubtree1(root.right, subRoot))
        
    def sameTree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        So sánh hai cây có giống hệt nhau không.
        """
        if not root and not subRoot:   # Cả 2 cùng rỗng => True
            return True
        if root and subRoot and root.val == subRoot.val:
            # So sánh tiếp nhánh trái và phải
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        return False

    # ---------------------- Cách 2: Serialize cây thành chuỗi ----------------------
    def isSubtree2(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        Serialize cây thành chuỗi và kiểm tra bằng substring matching.
        """
        string_s = self.traverse_tree(root)
        string_t = self.traverse_tree(subRoot)
        return string_t in string_s
    
    def traverse_tree(self, s: TreeNode) -> str:
        """
        Serialize cây theo dạng Pre-order traversal.
        Dùng 'X' để đánh dấu node null để tránh nhập nhằng.
        """
        if s is None:
            return "X"  # đánh dấu null
        return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"

# ---------------------- Test trong VS Code ----------------------
if __name__ == "__main__":
    # Tạo cây root = [3,4,5,1,2]
    root = TreeNode(3)
    root.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root.right = TreeNode(5)

    # Tạo subRoot = [4,1,2]
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

    s = Solution()

    print("Cách 1 (isSame + DFS):", s.isSubtree1(root, subRoot))  # ✅ True
    print("Cách 2 (Serialize + substring):", s.isSubtree2(root, subRoot))  # ✅ True

    # Test case sai
    subRoot2 = TreeNode(4, TreeNode(1), TreeNode(3))
    print("Cách 1 (isSame + DFS):", s.isSubtree1(root, subRoot2))  # ❌ False
    print("Cách 2 (Serialize + substring):", s.isSubtree2(root, subRoot2))  # ❌ False
