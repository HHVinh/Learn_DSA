from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # số hàng và số cột của board
        
        board_counter = Counter(ch for row in board for ch in row) # Đếm số lần xuất hiện của từng ký tự trong board
        word_counter = Counter(word) # Đếm số lần xuất hiện của từng ký tự trong từ word

        for ch in word_counter: # Nếu trong board thiếu ký tự cần thiết so với word => trả về False ngay
            if board_counter[ch] < word_counter[ch]:
                return False

        # Tối ưu: nếu ký tự đầu của word xuất hiện nhiều hơn ký tự cuối
        # thì ta đảo ngược word để bắt đầu tìm từ ký tự "ít phổ biến hơn"
        if board_counter[word[0]] > board_counter[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i): # Hàm DFS kiểm tra từ vị trí (r, c) có khớp tiếp tục với word[i:] hay không
            if i == len(word):  # nếu duyệt hết word thì thành công
                return True
            # Kiểm tra điều kiện ngoài biên hoặc ký tự không khớp
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            temp = board[r][c] # Đánh dấu ô đã dùng bằng ký tự đặc biệt '#'
            board[r][c] = '#'

            # Thử đi 4 hướng: xuống, lên, phải, trái
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            board[r][c] = temp # Hoàn tác (backtracking) để có thể dùng lại ô này cho nhánh khác
            return res

        for r in range(ROWS): # Duyệt từng ô trong board, thử bắt đầu từ ô đó
            for c in range(COLS):
                if dfs(r, c, 0):  # nếu tìm thấy thì trả về True
                    return True
        return False  # nếu duyệt hết mà không thấy thì False

# ================== Chương trình chính ==================
if __name__ == "__main__":
    # Cho sẵn board
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    
    # Nhập từ cần tìm
    word = input("Nhập từ cần tìm: ")

    sol = Solution()
    if sol.exist(board, word):
        print(f"Từ '{word}' CÓ trong bảng.")
    else:
        print(f"Từ '{word}' KHÔNG CÓ trong bảng.")
