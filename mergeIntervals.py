from typing import List   # Import để dùng List trong VS Code

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Nếu danh sách rỗng thì trả về ngay
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])   # Sắp xếp theo start của mỗi interval
        n = len(intervals)                   # Số lượng interval

        res = [intervals[0]]                 # res chứa interval đầu tiên đã sắp xếp

        for i in range(1, n):                # Duyệt từ interval thứ 2
            # Nếu interval hiện tại KHÔNG chồng với interval cuối trong res
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])     # Thêm interval mới vào res

            # Nếu bị chồng và interval hiện tại mở rộng hơn
            elif intervals[i][1] > res[-1][1]:
                res[-1][1] = intervals[i][1]  # Gộp bằng cách cập nhật end

        return res                            # Trả về danh sách đã gộp


# ====== TEST CHẠY TRONG VS CODE ======
if __name__ == "__main__":
    sol = Solution()

    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals1))   # [[1,6],[8,10],[15,18]]

    intervals2 = [[1,4],[4,5]]
    print(sol.merge(intervals2))   # [[1,5]]
