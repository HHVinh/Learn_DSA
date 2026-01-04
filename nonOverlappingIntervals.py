from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Nếu chỉ có 0 hoặc 1 interval thì không cần xóa cái nào
        if len(intervals) <= 1:
            return 0

        # Sắp xếp các interval theo thời điểm kết thúc (end)
        # x[1] là phần tử end của mỗi interval [start, end]
        # [[1,3],[2,4],[1,2]] → sort theo end → [[1,2],[1,3],[2,4]]
        intervals.sort(key=lambda x: x[1])

        # prevEnd: thời điểm kết thúc của interval đang được giữ
        prevEnd = intervals[0][1]

        # res: số interval cần xóa
        res = 0

        # Duyệt từ interval thứ 2 trở đi
        for i in range(1, len(intervals)):
            # Nếu interval hiện tại bắt đầu trước khi interval trước kết thúc
            # => bị chồng chéo
            if intervals[i][0] < prevEnd:
                # Ta buộc phải xóa interval này
                res += 1
            else:
                # Không chồng chéo → giữ lại
                # Cập nhật prevEnd sang end mới
                prevEnd = intervals[i][1]

        return res


# ================== PHẦN CHẠY TEST TRONG VS CODE ==================
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [[1,2],[2,3],[3,4],[1,3]],
        [[1,2],[1,2],[1,2]],
        [[1,2],[2,3]],
        [[1,100],[11,22],[1,11],[2,12]]
    ]

    for intervals in test_cases:
        print(f"Intervals: {intervals}")
        print("Số interval cần xóa:", sol.eraseOverlapIntervals(intervals))
        print("-" * 40)
