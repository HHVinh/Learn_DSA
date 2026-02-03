# Bài 36 
# Không gian (Space): O(N)
# Tốc độ (Time): Nhanh, nhưng chậm hơn Bitmask
# Khả năng mở rộng: Dùng được cho mọi loại dữ liệu (chữ, số lớn)

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]      # rows[i]: lưu các số đã xuất hiện ở hàng i
        cols = [set() for _ in range(9)]      # cols[j]: lưu các số đã xuất hiện ở cột j
        boxes = [set() for _ in range(9)]     # boxes[k]: lưu các số đã xuất hiện ở ô 3x3 thứ k

        for r in range(9):                    # duyệt từng hàng
            for c in range(9):                # duyệt từng cột
                val = board[r][c]             # lấy giá trị ô hiện tại

                if val == '.':                # nếu ô trống thì bỏ qua
                    continue

                box_index = (r // 3) * 3 + (c // 3)   # xác định ô vuông 3x3 chứa ô (r, c)

                if val in rows[r]:             # nếu số đã xuất hiện trong hàng
                    return False
                if val in cols[c]:             # nếu số đã xuất hiện trong cột
                    return False
                if val in boxes[box_index]:    # nếu số đã xuất hiện trong ô 3x3
                    return False

                rows[r].add(val)               # đánh dấu số đã xuất hiện ở hàng
                cols[c].add(val)               # đánh dấu số đã xuất hiện ở cột
                boxes[box_index].add(val)      # đánh dấu số đã xuất hiện ở ô 3x3

        return True                            # duyệt xong không lỗi → bảng hợp lệ


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
