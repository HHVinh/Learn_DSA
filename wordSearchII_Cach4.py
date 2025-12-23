from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)                     # số hàng của board
        n = len(board[0])                  # số cột của board
        self.ans = []                      # danh sách kết quả
        self.trie = {}                     # Trie dùng dict lồng nhau

        # =======================
        # 1️⃣ XÂY TRIE
        # =======================
        for word in words:
            node = self.trie               # bắt đầu từ gốc Trie
            for c in word:
                if c not in node:
                    node[c] = {}           # tạo node mới nếu chưa tồn tại
                node = node[c]             # đi xuống node con
            node['#'] = word               # '#' đánh dấu kết thúc 1 từ

        # =======================
        # 2️⃣ DFS TÌM TỪ
        # =======================
        def dfs(node, visit, x, y):
            if not node:                   # nếu node rỗng → không còn nhánh
                return

            # duyệt 4 hướng
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy

                # kiểm tra biên
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                # nếu ký tự tồn tại trong Trie và chưa đi qua
                if board[nx][ny] in node and not visit[nx][ny]:
                    visit[nx][ny] = True                   # đánh dấu đã đi
                    dfs(node[board[nx][ny]], visit, nx, ny)
                    visit[nx][ny] = False                  # backtracking

                    # nếu nhánh con rỗng thì xóa (pruning)
                    if not node[board[nx][ny]]:
                        node.pop(board[nx][ny])

            # nếu gặp kết thúc từ
            if '#' in node:
                self.ans.append(node['#'])  # thêm từ vào kết quả
                node.pop('#')               # xóa để tránh trùng lặp

        # =======================
        # 3️⃣ KHỞI CHẠY DFS
        # =======================
        visit = [[False] * n for _ in range(m)]  # mảng đánh dấu đã đi

        for i in range(m):
            for j in range(n):
                if board[i][j] not in self.trie:
                    continue                  # không có nhánh → bỏ qua

                visit[i][j] = True
                dfs(self.trie[board[i][j]], visit, i, j)
                visit[i][j] = False

        return self.ans


if __name__ == "__main__":
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]

    words = ["oath", "pea", "eat", "rain"]

    sol = Solution()
    result = sol.findWords(board, words)

    print("Các từ tìm được:")
    print(result)