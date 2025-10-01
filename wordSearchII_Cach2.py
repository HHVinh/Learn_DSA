from typing import List   # cần import List để chạy được annotation

# ------------------ Định nghĩa TrieNode ------------------
class TrieNode:
    def __init__(self):
        self.children = {}   # dict: key là ký tự, value là TrieNode con
        self.word = None     # nếu node này là điểm cuối của 1 từ, lưu từ đó


# ------------------ Lớp Solution ------------------
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Tạo Trie gốc
        root = TrieNode()
        m = len(board)   # số hàng
        n = len(board[0])  # số cột
        ans = set()   # dùng set để tránh kết quả trùng lặp

        # ------------------ Bước 1: Xây dựng Trie ------------------
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()  # thêm node mới nếu chưa có
                curr = curr.children[char]
            curr.word = word  # đánh dấu node cuối lưu từ

        # ------------------ Bước 2: DFS trên board ------------------
        def dfs(row, col, node):
            # Điều kiện dừng: ra ngoài board hoặc ô đã dùng rồi
            if not (0 <= row < m and 0 <= col < n) or board[row][col] == "*":
                return

            char = board[row][col]

            # Nếu ký tự này không có trong Trie -> dừng
            if char not in node.children:
                return

            # Di chuyển xuống node con trong Trie
            node = node.children[char]

            # Nếu node này là điểm cuối của 1 từ -> thêm vào kết quả
            if node.word:
                ans.add(node.word)   # thêm từ vào tập kết quả
                node.word = None     # gán None để tránh tìm lại cùng từ lần sau

            # Đánh dấu ô đã đi qua (backtracking)
            original = board[row][col]
            board[row][col] = "*"

            # DFS 4 hướng
            dfs(row + 1, col, node)  # xuống
            dfs(row - 1, col, node)  # lên
            dfs(row, col + 1, node)  # phải
            dfs(row, col - 1, node)  # trái

            # Khôi phục lại giá trị ban đầu (backtrack)
            board[row][col] = original

        # ------------------ Bước 3: Chạy DFS từ mọi ô ------------------
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        # ------------------ Bước 4: Trả về kết quả ------------------
        return list(ans)


# ------------------ Ví dụ chạy thử ------------------
if __name__ == "__main__":
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]

    sol = Solution()
    result = sol.findWords(board, words)
    print("Kết quả tìm được:", result)
