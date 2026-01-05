from typing import List

# Định nghĩa class Interval giống đề bài
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sắp xếp các cuộc họp theo thời điểm bắt đầu (start)
        intervals.sort(key=lambda i: i.start)

        # Duyệt từ cuộc họp thứ 2 trở đi
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # cuộc họp trước
            i2 = intervals[i]      # cuộc họp hiện tại

            # Nếu cuộc trước kết thúc sau khi cuộc hiện tại bắt đầu
            if i1.end > i2.start:
                return False  # chồng chéo

        return True


# ================== TEST VS CODE ==================
if __name__ == "__main__":
    sol = Solution()

    meetings = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
    ]

    print("Cách 2 - Sort theo start:")
    print(sol.canAttendMeetings(meetings))
