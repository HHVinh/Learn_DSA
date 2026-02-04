# Bài 36 
# Không gian (Space): O(1)
# Tốc độ (Time): Siêu nhanh
# Khả năng mở rộng: Chỉ dùng tốt khi dữ liệu là số nhỏ (1-9)

class Solution:
    def isValidSudoku(self, board):
        rows = [0] * 9                         # mỗi hàng là 1 số nguyên dùng làm bitmask
        cols = [0] * 9                         # mỗi cột là 1 số nguyên dùng làm bitmask
        squares = [0] * 9                      # mỗi ô 3x3 là 1 số nguyên dùng làm bitmask

        for r in range(9):                     # duyệt từng hàng
            for c in range(9):                 # duyệt từng cột
                if board[r][c] == ".":         # nếu ô trống thì bỏ qua
                    continue

                val = int(board[r][c]) - 1     # đổi '1'..'9' thành 0..8
                mask = 1 << val                # tạo bit đại diện cho số hiện tại

                if rows[r] & mask:             # kiểm tra bit đã bật trong hàng chưa
                    return False
                if cols[c] & mask:             # kiểm tra bit đã bật trong cột chưa
                    return False
                idx = (r // 3) * 3 + (c // 3)  # xác định ô vuông 3x3
                if squares[idx] & mask:        # kiểm tra bit đã bật trong ô 3x3 chưa
                    return False

                rows[r] |= mask                # bật bit tương ứng trong hàng
                cols[c] |= mask                # bật bit tương ứng trong cột
                squares[idx] |= mask            # bật bit tương ứng trong ô 3x3

        return True                            # không có trùng → bảng hợp lệ


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    sol = Solution()                           # tạo đối tượng Solution
    print(sol.isValidSudoku(board))            # in kết quả kiểm tra
