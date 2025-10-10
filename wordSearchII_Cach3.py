from typing import List

# Lớp TrieNode dùng để tạo cây Trie (cấu trúc dữ liệu lưu trữ từ)
class TrieNode:
    def __init__(self):
        # children là dictionary chứa các ký tự con (vd: {'a': TrieNode, 'b': TrieNode, ...})
        self.children = {}
        # word lưu lại từ đầy đủ khi một node là điểm kết thúc của từ
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Tạo gốc của cây Trie
        root = TrieNode()
        m, n = len(board), len(board[0])  # Kích thước bảng chữ cái
        res = set()  # Dùng set để tránh trùng từ

        # Bước 1: Xây dựng cây Trie từ danh sách từ cần tìm
        for word in words:
            cur = root
            for c in word:
                # Nếu ký tự chưa có trong Trie thì thêm vào
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            # Gán toàn bộ từ ở node cuối cùng
            cur.word = word
        
        # Bước 2: Hàm DFS để tìm từ trên bảng chữ cái
        def dfs(r, c, node):
            # Nếu vượt ra ngoài bảng hoặc ô đã được thăm rồi thì dừng
            if (not (0 <= r < m and 0 <= c < n) or board[r][c] == '*'):
                return
            
            char = board[r][c]  # Lấy ký tự tại vị trí hiện tại

            # Nếu ký tự không nằm trong Trie thì dừng lại
            if char not in node.children:
                return
            
            # Di chuyển xuống node con tương ứng trong Trie
            node = node.children[char]

            # Nếu node hiện tại chứa từ hoàn chỉnh → thêm vào kết quả
            if node.word:
                res.add(node.word)
                node.word = None  # Xóa để tránh trùng lặp
            
            # Đánh dấu ô hiện tại là đã thăm
            temp = board[r][c]
            board[r][c] = '*'

            # Gọi đệ quy 4 hướng
            dfs(r + 1, c, node)  # xuống
            dfs(r - 1, c, node)  # lên
            dfs(r, c + 1, node)  # phải
            dfs(r, c - 1, node)  # trái

            # Phục hồi ký tự sau khi quay lui
            board[r][c] = temp
        
        # Bước 3: Duyệt toàn bộ bảng để tìm từ bắt đầu tại mỗi vị trí
        for r in range(m):
            for c in range(n):
                dfs(r, c, root)

        # Trả về danh sách kết quả
        return list(res)


# --- Phần kiểm thử (bạn có thể chạy trực tiếp trong VS Code) ---
if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    
    sol = Solution()
    result = sol.findWords(board, words)
    print("Các từ tìm thấy:", result)
