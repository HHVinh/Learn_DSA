# -----------------------------
# Định nghĩa node của cây nhị phân
# -----------------------------
class TreeNode:
    def __init__(self, x):
        self.val = x       # Giá trị của node
        self.left = None   # Con trái
        self.right = None  # Con phải


# -----------------------------
# Lớp Codec dùng để mã hóa (serialize)
# và giải mã (deserialize) cây nhị phân
# -----------------------------
class Codec:

    # -----------------------------
    # Hàm serialize: chuyển cây -> chuỗi
    # -----------------------------
    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []  # Danh sách lưu thứ tự duyệt cây

        # Duyệt cây theo thứ tự tiền tự (preorder)
        def dfs(node):
            if not node:
                res.append("N")  # Nếu node rỗng, lưu "N"
                return
            res.append(str(node.val))  # Lưu giá trị node hiện tại
            dfs(node.left)   # Gọi đệ quy bên trái
            dfs(node.right)  # Gọi đệ quy bên phải

        dfs(root)
        return ",".join(res)  # Ghép danh sách thành chuỗi


    # -----------------------------
    # Hàm deserialize: chuyển chuỗi -> cây
    # -----------------------------
    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        val = data.split(",")  # Tách chuỗi thành danh sách
        self.i = 0             # Con trỏ chỉ vị trí hiện tại trong danh sách

        # Duyệt theo thứ tự đã lưu để tạo lại cây
        def dfs():
            # Nếu gặp ký hiệu "N" -> node rỗng
            if val[self.i] == "N":
                self.i += 1
                return None

            # Tạo node mới với giá trị hiện tại
            node = TreeNode(int(val[self.i]))
            self.i += 1

            # Gọi đệ quy tạo cây con trái và phải
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# -----------------------------
# Chạy thử chương trình
# -----------------------------
if __name__ == "__main__":
    # Tạo cây mẫu:
    #         1
    #        / \
    #       2   3
    #          / \
    #         4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Tạo đối tượng Codec
    codec = Codec()

    # Mã hóa cây
    serialized = codec.serialize(root)
    print("Chuỗi sau khi serialize:", serialized)

    # Giải mã chuỗi thành cây
    deserialized_root = codec.deserialize(serialized)

    # Kiểm tra: in lại cây theo preorder sau khi deserialize
    def printPreorder(node):
        if not node:
            print("N", end=" ")
            return
        print(node.val, end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

    print("Cây sau khi deserialize (duyệt preorder):", end=" ")
    printPreorder(deserialized_root)
