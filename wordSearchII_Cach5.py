from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])          # m: số hàng, n: số cột của board
        self.ans = []                             # Lưu các từ tìm được
        self.trie = {}                            # Trie dạng dictionary
        # ========== XÂY TRIE ==========
        for word in words:                        # Duyệt từng từ trong words
            cur = self.trie                       # Bắt đầu từ gốc Trie
            for c in word:                        # Duyệt từng ký tự của từ
                if c not in cur:                  # Nếu chưa có node ký tự
                    cur[c] = {}                   # Tạo node mới
                cur = cur[c]                      # Đi xuống node con
            cur["#"] = word                       # Đánh dấu kết thúc từ
        # ========== DFS ==========
        def dfs(node, r, c):
            if "#" in node:                       # Nếu node hiện tại kết thúc 1 từ
                self.ans.append(node["#"])        # Lưu từ vào kết quả
                node.pop("#")                     # Xóa để tránh trùng kết quả

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:  # 4 hướng
                nr, nc = r + dr, c + dc           # Tọa độ mới
                if 0 <= nr < m and 0 <= nc < n and not visit[nr][nc]:  # Kiểm tra hợp lệ
                    ch = board[nr][nc]            # Lấy ký tự tại ô mới

                    if ch in node:                # Nếu ký tự tồn tại trong Trie
                        visit[nr][nc] = True      # Đánh dấu đã đi
                        dfs(node[ch], nr, nc)     # DFS sang node con
                        visit[nr][nc] = False     # Backtrack

                        if not node[ch]:          # Nếu node con rỗng
                            node.pop(ch)          # Cắt nhánh Trie (tối ưu)
        # ========== DUYỆT TỪNG Ô LÀM ĐIỂM BẮT ĐẦU ==========
        visit = [[False] * n for _ in range(m)]   # Mảng đánh dấu ô đã đi qua
        for r in range(m):                         # Duyệt từng hàng
            for c in range(n):                     # Duyệt từng cột
                ch = board[r][c]                   # Ký tự hiện tại

                if ch in self.trie:                # Nếu ký tự tồn tại trong Trie
                    visit[r][c] = True             # Đánh dấu đã đi
                    dfs(self.trie[ch], r, c)       # Bắt đầu DFS
                    visit[r][c] = False            # Backtrack
        return self.ans                            # Trả về danh sách từ tìm được


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