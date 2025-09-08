from collections import deque
from typing import Optional
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val       # giá trị của node
        self.left = left     # con trái
        self.right = right   # con phải

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str: # Hàm chuyển cây thành chuỗi (serialize)
        if not root:
            return "N"  # Nếu cây rỗng thì trả về "N"
        
        res = []  
        queue = deque([root])  # Dùng BFS (queue)

        while queue:
            node = queue.popleft()

            if not node:
                res.append("N")  # Node rỗng
            else:
                res.append(str(node.val))  # Lưu giá trị node
                queue.append(node.left)    # Thêm con trái vào queue
                queue.append(node.right)   # Thêm con phải vào queue
        
        return ",".join(res)  # Ghép thành chuỗi cách nhau bằng dấu phẩy

    def deserialize(self, data: str) -> Optional[TreeNode]: # Hàm dựng lại cây từ chuỗi (deserialize)
        vals = data.split(",")  # Tách chuỗi thành danh sách

        if vals[0] == "N":
            return None  # Nếu chuỗi chỉ là "N" thì cây rỗng
        
        root = TreeNode(int(vals[0]))  # Tạo root
        queue = deque([root])          # Queue để xử lý BFS
        index = 1                      # Vị trí đang xét trong danh sách

        while queue:
            node = queue.popleft()
            
            if vals[index] != "N": # Xử lý con trái
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            
            # Xử lý con phải
            if vals[index] != "N": # Xử lý con phải
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        
        return root

# ================== TEST ==================
if __name__ == "__main__":
    # Tạo cây mẫu:
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    codec = Codec()
    
    # Serialize cây -> chuỗi
    data = codec.serialize(root)
    print("Serialize:", data)
    
    # Deserialize chuỗi -> cây
    new_root = codec.deserialize(data)
    print("Deserialize -> In lại root:", new_root.val)           # 1
    print("Con trái của root:", new_root.left.val)               # 2
    print("Con phải của root:", new_root.right.val)              # 3
    print("Con trái của node 3:", new_root.right.left.val)       # 4
    print("Con phải của node 3:", new_root.right.right.val)      # 5
