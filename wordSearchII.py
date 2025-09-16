from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # lưu 26 chữ cái a-z
        self.idx = -1                # vị trí từ trong mảng words
        self.refs = 0                # số lần tham chiếu (bao nhiêu từ đi qua node này)

    def addWord(self, word, i):
        cur = self
        cur.refs += 1                # node gốc cũng có thêm 1 từ đi qua
        for c in word:               # duyệt từng ký tự trong word
            index = ord(c) - ord('a')  # tính chỉ số 0-25
            if not cur.children[index]:  # nếu chưa có node con thì tạo
                cur.children[index] = TrieNode()
            cur = cur.children[index]   # đi tiếp xuống node con
            cur.refs += 1               # tăng số từ đi qua node này
        cur.idx = i                     # đánh dấu node cuối là 1 từ hợp lệ

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):   # thêm tất cả words vào trie
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])  # số hàng, số cột
        res = []  # lưu kết quả

        def getIndex(c):
            return ord(c) - ord('a')  # đổi chữ cái thành số (0-25)

        def dfs(r, c, node):
            # điều kiện dừng: ra khỏi bảng, gặp ô đã thăm '*', hoặc không có node con
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] == '*' or not node.children[getIndex(board[r][c])]):
                return

            tmp = board[r][c]              # lưu lại chữ cái hiện tại
            board[r][c] = '*'              # đánh dấu đã thăm
            prev = node                    # node cha
            node = node.children[getIndex(tmp)]  # node con tương ứng ký tự

            if node.idx != -1:             # tìm thấy 1 từ hoàn chỉnh
                res.append(words[node.idx])  # thêm từ vào kết quả
                node.idx = -1                # tránh trùng lặp
                node.refs -= 1               # giảm tham chiếu
                if not node.refs:            # nếu node này ko còn từ nào
                    prev.children[getIndex(tmp)] = None  # xóa node
                    node = None
                    board[r][c] = tmp        # backtrack: khôi phục chữ cái
                    return

            # tiếp tục tìm 4 hướng
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = tmp  # backtrack: khôi phục chữ cái

        # chạy dfs từ tất cả ô trong board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res

# ---------------------------
# Ví dụ test trong VS Code:
if __name__ == "__main__":
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]
    sol = Solution()
    print(sol.findWords(board, words))  # 👉 ['oath', 'eat']
