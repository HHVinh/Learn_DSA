# Lớp đại diện cho 1 nút trong cây Trie
class TrieNode:
    def __init__(self):
        # Mỗi nút có 26 phần tử con, tương ứng 26 chữ cái a–z
        self.children = [None] * 26
        # endOfWord = True nếu nút này là điểm kết thúc của 1 từ hợp lệ
        self.endOfWord = False


# Lớp đại diện cho cây Trie (cây tiền tố)
class PrefixTree:
    def __init__(self):
        # Khởi tạo gốc của cây (trống)
        self.root = TrieNode()

    # -------------------------------
    # 1️⃣ Thêm một từ vào cây
    # -------------------------------
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")  # chuyển chữ cái thành chỉ số (0–25)
            if cur.children[i] is None:
                cur.children[i] = TrieNode()  # tạo nút mới nếu chưa có
            cur = cur.children[i]
        # Đánh dấu nút cuối là kết thúc 1 từ
        cur.endOfWord = True

    # -------------------------------
    # 2️⃣ Kiểm tra xem 1 từ có tồn tại trong cây không
    # -------------------------------
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                return False  # không tìm thấy ký tự trong cây
            cur = cur.children[i]
        # Chỉ trả về True nếu đây là điểm kết thúc của 1 từ hoàn chỉnh
        return cur.endOfWord

    # -------------------------------
    # 3️⃣ Kiểm tra xem có từ nào bắt đầu với prefix này không
    # -------------------------------
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        # Nếu duyệt hết prefix mà không bị ngắt -> có từ bắt đầu bằng prefix này
        return True


# -------------------------------
# 🔍 Ví dụ sử dụng:
# -------------------------------
trie = PrefixTree()
trie.insert("apple")
trie.insert("app")

print(trie.search("apple"))     # ✅ True  -> 'apple' có trong cây
print(trie.search("app"))       # ✅ True  -> 'app' cũng là 1 từ hoàn chỉnh
print(trie.search("appl"))      # ❌ False -> chỉ là tiền tố, chưa đánh dấu kết thúc từ
print(trie.startsWith("appl"))  # ✅ True  -> có từ bắt đầu bằng 'appl'
print(trie.startsWith("bat"))   # ❌ False -> không có từ nào bắt đầu bằng 'bat'
